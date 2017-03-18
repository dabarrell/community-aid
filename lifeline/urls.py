from django.conf.urls import url

from . import views

app_name = 'lifeline'

urlpatterns = [
    url(r'^$', views.index, name='index'),
	url(r'^map/$', views.map, name ="map"),
	url(r'^news_feed/$', views.news_feed, name ="news_feed"),
	url(r'^item/(?P<item_id>[0-9]+)/$', views.item, name='item'),
	url(r'^login/$', views.login, name ="login"),
	url(r'^create/$', views.create, name ="create"),
	url(r'^submitted/$', views.submitted, name='submitted'),
]
