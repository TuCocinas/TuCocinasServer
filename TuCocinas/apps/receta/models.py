from __future__ import unicode_literals

# -*- encoding: utf-8 -*-
from django.contrib.auth.models import User
from TuCocinas.apps.base.models import *
from django.http import HttpResponse
from django.db import models
import json

class Receta(models.Model):
	usuario = models.ForeignKey(User)
	nombre_receta = models.CharField(max_length = 80)
	descripcion_receta = models.CharField(max_length = 200)
	calificacion_receta = models.IntegerField()
	preparacion_receta = models.CharField(max_length = 2000)
	tiempo_preparacion_receta = models.CharField(max_length = 5)
	dificultad_receta = models.ForeignKey(Dificultad)
	porciones_receta = models.CharField(max_length = 2)
	foto_receta = models.ImageField(upload_to = 'img/recetas/')
	categoria_receta = models.ForeignKey(Categoria)
	tipo_receta = models.ForeignKey(Tipo)

	def usuario_nombre(self):
		return self.usuario.first_name+' '+self.usuario.last_name

	def dificultad_receta_nombre(self):
		return {
			'dificultad': self.dificultad_receta.nombre_dificultad, 
			'nivel': self.dificultad_receta.slug_dificultad
		}

	def categoria_receta_nombre(self):
		return self.categoria_receta.nombre_categoria

	def tipo_receta_nombre(self):
		return self.tipo_receta.nombre_tipo

	def receta_url_imagen(self):
		return 'static/'+self.foto_receta.url

	def __str__(self):
		return self.nombre_receta

	def __unicode__(self):
		return self.nombre_receta

class ComentarioReceta(models.Model):
	usuario = models.ForeignKey(User)
	receta = models.ForeignKey(Receta)
	comentario_receta = models.CharField(max_length = 200)

class IngredienteReceta(models.Model):
	ingrediente = models.ForeignKey(Ingrediente)
	receta = models.ForeignKey(Receta)
	cantidad = models.DecimalField(max_digits = 6, decimal_places = 2)
