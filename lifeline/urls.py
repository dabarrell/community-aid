from django.conf.urls import url, include
from django.contrib.auth.views import auth_logout

from . import views

app_name="lifeline"

urlpatterns = [
    url(r'^$', views.index, name='index'),
        # ex: /lifeline/map/
	url(r'^map/$', views.map,name="map"),
	url(r'^item/(?P<item_id>[0-9a-f\-]+)/$', views.item, name='item'),
	url(r'^create/$', views.create,name="create"),
	url(r'^submitted/$', views.submitted, name="submitted"),
	url(r'^comment_submitted/$', views.comment_submitted, name="comment_submitted"),
	url(r'^logout/$', views.logout_view, name="logout_view"),
	url(r'^register/$', views.register, name="register"),
	url(r'^registerComplete/$', views.registerComplete, name="registerComplete"),
	url(r'^profile/$', views.profile, name="profile"),
    url('^', include('django.contrib.auth.urls'))
]
