from rest_framework import serializers
from .models import *

class RecetaSerializer(serializers.ModelSerializer):
	usuario_nombre = serializers.ReadOnlyField()
	dificultad_receta_nombre = serializers.ReadOnlyField()
	categoria_receta_nombre = serializers.ReadOnlyField()
	tipo_receta_nombre = serializers.ReadOnlyField()

	class Meta:
		model = Receta
		fields = (
			'nombre_receta', 
			'descripcion_receta',
			'calificacion_receta',
			'preparacion_receta',
			'tiempo_preparacion_receta',
			'dificultad_receta_nombre',
			'porciones_receta',
			'receta_url_imagen',
			'categoria_receta_nombre',
			'usuario_nombre', 
			'tipo_receta_nombre'
		)