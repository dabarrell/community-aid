from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader

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
	response = "You're looking at the details of item %s"
	return HttpResponse(response % item_id)

def submitted(request):
	context = {"item_name":request.POST.get("item_name")}
	template = loader.get_template('lifeline/submitted.html')

	return HttpResponse(template.render(context, request))

def map(request):
	return HttpResponse("This is the map")

def create(request):


	#priorities = Item_Priorities.objects.all()
	priorities = ["Critical", "Medium", "Low"]
	categories = ["Food", "Water", "Electricity", "Supplies", "Infrastructure", "Equipment", "Repairs", "Emergency", "Hazard"]
	types = ["Request", "Offer", "Alert"]
	template = loader.get_template('lifeline/create.html')
	context = {
		'priorities': priorities,
		'categories': categories,
		'types': types,
	}
	return HttpResponse(template.render(context, request))
