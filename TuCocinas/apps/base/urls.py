from django.conf.urls import patterns, url, include
from .views import *

urlpatterns = patterns('TuCocinas.apps.base.views',
	url(r'^data/$', DataInitial.as_view(), name = 'data_initial'),
)