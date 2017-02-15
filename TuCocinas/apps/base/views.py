from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import HttpResponse
from .serializers import *
from .models import *

class DataInitial(APIView):
	permission_classes = (AllowAny,)

	def get(self, request, format = None):
		response = {}
		response['dificultad'] = DificultadSerializer(Dificultad.objects.all(), many = True).data
		response['tipo'] = TipoSerializer(Tipo.objects.all(), many = True).data
		response['categoria'] = CategoriaSerializer(Categoria.objects.all(), many = True).data
		return Response(response)