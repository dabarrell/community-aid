from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.db import models
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login

from django.contrib.auth.models import User as DefaultUser
from .models import Item_Category, Item, User, Item_Type
from .utils import distance, distanceWrapper, sendMessage

from django.db.models import Q

#max display distance
max_distance = 10

def index(request):

	#default sort key is by time
	sort_key = 'created_at'
	reverse = False
	filters = ['offer', 'request', 'alert']

	if request.POST.get("sort_key"):
		sort_key = request.POST.get("sort_key")
	if request.POST.get("filter"):
		filters = request.POST.getlist("filter")

	f1 = -1
	f2 = -1
	f3 = -1

	if 'offer' in filters:
		f1 = Item_Type.objects.get(type_name='Offer').id

	if 'request' in filters:
		f2 = Item_Type.objects.get(type_name='Request').id

	if 'alert' in filters:
		f3 = Item_Type.objects.get(type_name='Alert').id

	unsorted_items = Item.objects.filter(Q(item_type= f1) | Q(item_type = f2) | Q(item_type = f3))

	#default long and lat
	userlat = -37.8001775
	userlng = 144.9640978

	if request.POST.get("latitude"):
		userlat = request.POST.get("latitude")
		userlng = request.POST.get("longitude")
	for item in unsorted_items:
		item.distance = "%.1f" % distanceWrapper(item, userlat, userlng)
		item.distanceFlt = distanceWrapper(item, userlat, userlng)

	if sort_key == "distance":
		print("Sort by distance")
		items = sorted(unsorted_items, key= lambda item: item.distanceFlt)
		if reverse:
			items = list(reversed(items))
	elif sort_key == "created_at":
		print("Sort by time")
		items = sorted(unsorted_items, key= lambda item: item.created_at)
		if not reverse:
			items = list(reversed(items))
	elif sort_key == "item_priority":
		print("Sort by priority")
		items = sorted(unsorted_items, key= lambda item: item.item_priority.id)
		if reverse:
			items = list(reversed(items))

	def distance_filter(element):
		return element.distanceFlt < max_distance
	items = filter(distance_filter, items)



	template = loader.get_template('lifeline/index.html')
	context = {
		'items': items,
		'lat': request.POST.get("latitude"),
		'lng': request.POST.get("longitude"),
		'sort_key': sort_key,
		'filters': filters
	}
	print(context)
	return HttpResponse(template.render(context, request))

def item(request, item_id):

	item = item_id

	context = {
		'item_id': item,
		'item_name': Item.objects.get(pk=item).item_name,
		'item_description': Item.objects.get(pk=item).item_description,
		'item_priority': Item.objects.get(pk=item).item_priority,
		'item_category': Item.objects.get(pk=item).item_category,
		'item_type': Item.objects.get(pk=item).item_type,
		'item_longitude': Item.objects.get(pk=item).item_longitude,
		'item_latitude': Item.objects.get(pk=item).item_latitude,
		'comments' : Comment.objects.filter(item_id=item).order_by('created_at')

	}
	template = loader.get_template('lifeline/item.html')

	return HttpResponse(template.render(context, request))

@login_required
def submitted(request):
	user = User.objects.get(user=request.user)
	context = {"item_name":request.POST.get("item_name")}
	submit_item(request.POST, user)
	template = loader.get_template('lifeline/submitted.html')

	return HttpResponse(template.render(context, request))

@login_required
def comment_submitted(request):

	user = User.objects.get(user=request.user)
	context = {
		"comment_text":request.POST.get("comment_text"),
		"item":request.POST.get("item")
		}
	submit_comment(request.POST, user)

	return redirect("/item/"+request.POST.get("item"))

def map(request):
	items = Item.objects.all()
	context = { "items": items }
	template = loader.get_template('lifeline/map.html')
	return HttpResponse(template.render(context, request))

@login_required
def create(request):
	user = User.objects.get(user=request.user)

	categories = Item_Category.objects.all()
	priorities = Item_Priority.objects.all()
	types = Item_Type.objects.all()

	template = loader.get_template('lifeline/create.html')
	context = {
		'priorities': priorities,
		'categories': categories,
		'types': types,
		'user' : user,
	}
	return HttpResponse(template.render(context, request))

@login_required
def profile(request):
	user = User.objects.get(user=request.user)

	template = loader.get_template('lifeline/profile.html')
	context = {
		'user' : user
	}
	return HttpResponse(template.render(context, request))

def register(request):
	template = loader.get_template('registration/register.html')
	context = { }
	return HttpResponse(template.render(context, request))

def registerComplete(request):
	print(request.POST.get("username"))
	username = request.POST.get("username")
	firstname = request.POST.get("firstname")
	lastname = request.POST.get("lastname")
	phone = request.POST.get("phone")
	email = request.POST.get("email")
	password = request.POST.get("password")

	defaultUser = DefaultUser.objects.create_user(username, email, password)
	defaultUser.last_name = lastname
	defaultUser.first_name = firstname
	defaultUser.email = email
	defaultUser.save()

	user = User (
		user = defaultUser,
		phone = phone
	)
	user.save()
	login(request, defaultUser)
	return redirect('/')

def logout_view(request):
	logout(request)
	return redirect('/')

def submit_item(post, user):

	priority_string = post.get('item_priority')
	category_string = post.get('item_category')
	print(post.get('item_category'))
	type_string = post.get('item_type')

	item = Item(
		item_name=post.get('item_name'),
		item_description=post.get('item_description'),
		user=user,
		item_latitude=post.get('latitude'),
		item_longitude=post.get('longitude'),
		item_priority=Item_Priority.objects.get(priority_name=priority_string),
		item_category=Item_Category.objects.get(category_name=category_string),
		item_type=Item_Type.objects.get(type_name=type_string),

	)
	item.save()

def submit_comment(post,user):
	item = Item.objects.get(pk=post.get('item'))
	message = 'New comment on your request: ' + post.get('comment_text')
	sendMessage(message, item.user.phone)

	comment = Comment(
		item_id = post.get('item'),
		comment_text = post.get('comment_text'),
		user = user
	)
	comment.save()
