from django.contrib import admin

from .models import Actividades

class ActividadesAdmin(admin.ModelAdmin):
	list_display = ('fecha', 'tarea', 'Descripcion', 'usuario')
	list_filter = ('usuario',)
	search_fields = ['tarea__description', 'Descripcion']

admin.site.register (Actividades, ActividadesAdmin)