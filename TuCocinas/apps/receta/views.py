from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from django.shortcuts import render
from django.core import serializers
from .pagination import *
from .serializer import *
from .models import *

class RecetaList(ListAPIView):
	serializer_class = RecetaSerializer
	pagination_class = PaginatioLimitReceta

	def get_queryset(self, *args, **kwargs):
		recetas = Receta.objects.all()
		return recetas