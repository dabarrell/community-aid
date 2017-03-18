from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Item_Category

# Create your views here.
def index(request):
	categories = Item_Category.objects.all()
	template = loader.get_template('lifeline/index.html')
	context = {
		'categories': categories,
	}
	return HttpResponse(template.render(context, request))


def news_feed(request):
	return HttpResponse("This is the news feed")

def item(request, item_id):
	response = "You're looking at the details of item %s"
	return HttpResponse(response % item_id)

def submitted(request):
	context = {"item_name":request.POST.get("item_name")}
	template = loader.get_template('lifeline/submitted.html')

	return HttpResponse(template.render(context, request))

def map(request):
	return HttpResponse("This is the map")

def login(request):
	return HttpResponse("This is the login page")

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
