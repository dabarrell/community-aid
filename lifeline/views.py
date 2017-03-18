from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("YEAAAAH")


def news_feed(request):
	return HttpResponse("This is the news feed")

def item(request, item_id):
	response = "You're looking at the details of item %s"
	return HttpResponse(response % item_id)

def map(request):
	return HttpResponse("This is the map")

def login(request):
	return HttpResponse("This is the login page")

def create(request):
	return HttpResponse("This is the item creation page")