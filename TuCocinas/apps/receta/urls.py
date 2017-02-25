from django.views.decorators.csrf import csrf_exempt
from django.conf.urls import patterns, url, include
from .views import *

urlpatterns = patterns('TuCocinas.apps.receta.views',
	url(r'^nuevo/$', RecetaNew.as_view(), name = 'nuevo_receta'),
	url(r'^lista/$', RecetaList.as_view(), name = 'lista_receta'),
	url(r'^detalle/$', RecetaDetail.as_view(), name = 'detalle_receta'),
	url(r'^like-heart/$', HeartLikeReceta.as_view(), name = 'like_heart'),
)