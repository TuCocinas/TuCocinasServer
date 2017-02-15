from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import Q
from .serializers import *
from .pagination import *
from .models import *

class RecetaList(ListAPIView):
	serializer_class = RecetaSerializer
	pagination_class = PaginatioLimitReceta
	permission_classes = (AllowAny,)

	def get_queryset(self, *args, **kwargs):
		search = self.request.query_params.get('search', None)
		tipo = self.request.query_params.get('tipo', None)
		categoria = self.request.query_params.get('categoria', None)
		dificultad = self.request.query_params.get('dificultad', None)
		orden = self.request.query_params.get('orden', None)
		queryset = Receta.objects.all().order_by('-id')
		if(search is not None and search != ''):
			queryset = queryset.filter(Q(nombre_receta__icontains = search) | Q(descripcion_receta__icontains = search))
		if(tipo is not None and tipo != ''):
			queryset = queryset.filter(tipo_receta__slug_tipo = tipo)
		if(categoria is not None and categoria != ''):
			queryset = queryset.filter(categoria_receta__slug_categoria = categoria)
		if(dificultad is not None and dificultad != ''):
			queryset = queryset.filter(dificultad_receta__slug_dificultad = dificultad)
		if(orden == 'desc'):
			queryset = queryset.order_by('-nombre_receta')
		if(orden == 'asc'):
			queryset = queryset.order_by('nombre_receta')
		return queryset

class RecetaDetail(APIView):
	serializer_class = RecetaSerializer
	permission_classes = (AllowAny,)

	def get(self, request, format = None):
		receta = Receta.objects.get(slug_receta = self.request.query_params.get('slug_receta', None))
		return Response(RecetaSerializer(receta).data)

class HeartLikeReceta(APIView):

	def get(self, request, format = None):
		response = {}
		user_data = Token.objects.get(key = self.request.META['HTTP_TOKEN'])
		receta = Receta.objects.get(slug_receta = self.request.query_params.get('receta', None))
		if(receta.heart_like_receta.filter(auth_token = user_data.pk).exists()):
			receta.heart_like_receta.remove(user_data.user)
			receta.save()
		else:
			receta.heart_like_receta.add(user_data.user)
		return Response(response)