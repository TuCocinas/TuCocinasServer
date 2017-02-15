from django.views.decorators.csrf import csrf_exempt
from django.conf.urls import patterns, url, include
from .views import *

urlpatterns = patterns('TuCocinas.apps.users.views',
	url(r'^signup/$', csrf_exempt(UsersCreate.as_view()), name = 'signup'),
	url(r'^login/$', CustomObtainAuthToken.as_view(), name = 'login'),
	##url(r'^', include('rest_auth.urls')),
)