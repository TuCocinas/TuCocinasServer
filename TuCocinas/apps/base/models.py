from __future__ import unicode_literals

# -*- encoding: utf-8 -*-
from django.db import models

class Tipo(models.Model):
	nombre_tipo = models.CharField(max_length = 45)
	slug_tipo = models.CharField(max_length = 50)

	def __str__(self):
		return self.nombre_tipo

	def __unicode__(self):
		return self.nombre_tipo

class Categoria(models.Model):
	nombre_categoria = models.CharField(max_length = 45)
	slug_categoria = models.CharField(max_length = 50)

	def __str__(self):
		return self.nombre_categoria

	def __unicode__(self):
		return self.nombre_categoria

class Dificultad(models.Model):
	nombre_dificultad = models.CharField(max_length = 45)
	slug_dificultad = models.CharField(max_length = 50)

	def __str__(self):
		return self.nombre_dificultad

	def __unicode__(self):
		return self.nombre_dificultad

class Medida(models.Model):
	nombre_medida = models.CharField(max_length = 45)
	prefijo_medida = models.CharField(max_length = 3)

	def __str__(self):
		return self.nombre_medida

	def __unicode__(self):
		return self.nombre_medida

class Ingrediente(models.Model):
	nombre_ingrediente = models.CharField(max_length = 45)
	medida_ingrediente = models.ForeignKey(Medida)

	def __str__(self):
		return self.nombre_ingrediente

	def __unicode__(self):
		return self.nombre_ingrediente