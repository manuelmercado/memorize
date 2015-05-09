from django.contrib import admin

from .models import Actividades

class ActividadesAdmin(admin.ModelAdmin):
	list_display = ('fecha', 'tarea', 'Descripcion', 'usuario')

admin.site.register (Actividades, ActividadesAdmin)