from __future__ import unicode_literals

# -*- encoding: utf-8 -*-
# -*- decoding: utf-8 -*-
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from TuCocinas.apps.base.models import *
from django.http import HttpResponse
from django.db import models
import json

class Receta(models.Model):
	usuario = models.ForeignKey(User)
	nombre_receta = models.CharField(max_length = 80)
	slug_receta = models.CharField(max_length = 120)
	descripcion_receta = models.CharField(max_length = 500)
	tiempo_preparacion_receta = models.CharField(max_length = 5)
	dificultad_receta = models.ForeignKey(Dificultad)
	porciones_receta = models.CharField(max_length = 2)
	foto_receta = models.ImageField(upload_to = 'img/recetas/')
	categoria_receta = models.ForeignKey(Categoria)
	tipo_receta = models.ForeignKey(Tipo)
	heart_like_receta = models.ManyToManyField(User, blank = True, related_name = 'heart_like_receta')
	star_like_receta = models.ManyToManyField(User, blank = True, related_name = 'star_like_receta')

	def usuario_nombre(self):
		return {
			'user_full_name': self.usuario.first_name+' '+self.usuario.last_name,
			'token': Token.objects.get(user = self.usuario.pk).pk
		}

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

	def heart_like_receta_user(self):
		return [user_token.email for user_token in self.heart_like_receta.all()]

	def calificacion_receta(self):
		return self.heart_like_receta.count()

	def preparacion_receta(self):
		return [{'orden_paso': paso.orden_paso, 'foto_paso': 'static/'+paso.foto_paso.url if paso.foto_paso and hasattr(paso.foto_paso, 'url') else '', 'descripcion_paso': paso.descripcion_paso} for paso in self.recetapaso_set.all()]

	def ingrediente_receta(self):
		return [{'ingrediente': ingrediente.ingrediente.nombre_ingrediente, 'cantidad': ingrediente.cantidad, 'medida': ingrediente.ingrediente.medida_ingrediente} for ingrediente in self.ingredientereceta_set.all()]

	def __str__(self):
		return self.nombre_receta

	def __unicode__(self):
		return self.nombre_receta

class RecetaPaso(models.Model):
	receta = models.ForeignKey(Receta)
	orden_paso = models.CharField(max_length = 1)
	foto_paso = models.ImageField(upload_to = 'img/recetas/pasos/', blank = True, null = True)
	descripcion_paso = models.CharField(max_length = 1000)

	def __str__(self):
		return self.descripcion_paso

	def __unicode__(self):
		return self.descripcion_paso

class ComentarioReceta(models.Model):
	usuario = models.ForeignKey(User)
	receta = models.ForeignKey(Receta)
	comentario_receta = models.CharField(max_length = 200)

	def __str__(self):
		return self.comentario_receta

	def __unicode__(self):
		return self.comentario_receta

class IngredienteReceta(models.Model):
	ingrediente = models.ForeignKey(Ingrediente)
	receta = models.ForeignKey(Receta)
	cantidad = models.DecimalField(max_digits = 6, decimal_places = 2)
