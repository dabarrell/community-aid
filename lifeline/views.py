from django.shortcuts import render, redirect
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

def map(request):
	return HttpResponse("This is the map")

def create(request):
	return HttpResponse("This is the item creation page")
