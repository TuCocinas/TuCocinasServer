from rest_framework import serializers
from .models import *

class DificultadSerializer(serializers.ModelSerializer):

	class Meta:
		model = Dificultad
		fields = '__all__'

class TipoSerializer(serializers.ModelSerializer):

	class Meta:
		model = Tipo
		fields = '__all__'

class CategoriaSerializer(serializers.ModelSerializer):

	class Meta:
		model = Categoria
		fields = '__all__'