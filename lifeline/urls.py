from django.conf.urls import url, include
from django.contrib.auth.views import login

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
        # ex: /lifeline/map/
	url(r'^map/$', views.map),
	url(r'^news_feed/$', views.news_feed),
	url(r'^item/(?P<item_id>[0-9]+)/$', views.item, name='vote'),
	url(r'^create/$', views.create),
    url('^', include('django.contrib.auth.urls'))
]
