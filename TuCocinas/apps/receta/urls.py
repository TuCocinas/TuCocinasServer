from django.conf.urls import patterns, url, include
from .views import *

urlpatterns = patterns('TuCocinas.apps.receta.views',
	url(r'^lista/$', RecetaList.as_view(), name = 'lista_recetas'),
)