from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.db import models
from .models import *


from .models import Item_Category, Item

# Create your views here.
def index(request):
	items = Item.objects.all()
	template = loader.get_template('lifeline/index.html')
	context = {
		'items': items,
	}
	return HttpResponse(template.render(context, request))


def item(request, item_id):
	DUMMY_ID='7f8de92e-efc2-4c69-8f48-8612fab4b3a6'
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
		'comments' : Comment.objects.filter(item_id=item)

	}
	template = loader.get_template('lifeline/item.html')

	return HttpResponse(template.render(context, request))

def submitted(request):
	context = {"item_name":request.POST.get("item_name")}
	submit_item(request.POST)
	template = loader.get_template('lifeline/submitted.html')

	return HttpResponse(template.render(context, request))

def map(request):
	items = Item.objects.all()
	context = { "items": items }
	template = loader.get_template('lifeline/map.html')
	return HttpResponse(template.render(context, request))

def create(request):
	user = request.user
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


#make the user added to this
def submit_item(post):

	priority_string = post.get('item_priority')
	category_string = post.get('item_category')
	print(post.get('item_category'))
	type_string = post.get('item_type')

	item = Item(
		item_name=post.get('item_name'),
		item_description=post.get('item_description'),
		user=post.get('user'),
		item_latitude=post.get('latitude'),
		item_longitude=post.get('longitude'),
		item_priority=Item_Priority.objects.get(priority_name=priority_string),
		item_category=Item_Category.objects.get(category_name=category_string),
		item_type=Item_Type.objects.get(type_name=type_string),

	)#=post.get('item_name'))
	item.save()


#add datetime

def submit_comment(post,user):
	comment = Comment(
		item_id = post.get('item'),
		comment_text = post.get('comment_text'),
		user = user
	)
	comment.save()
