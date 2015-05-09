from django.contrib import admin

from .models import Tareas


class TareasAdmin(admin.ModelAdmin):    
    list_display = ('description', 'date_tarea', 'owner', 'state')

admin.site.register(Tareas, TareasAdmin)