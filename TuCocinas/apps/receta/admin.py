from django.contrib import admin
from .models import *

admin.site.register(Receta)
admin.site.register(ComentarioReceta)
admin.site.register(IngredienteReceta)