from django.contrib import admin

from .models import Tareas


class TareasAdmin(admin.ModelAdmin):    
    list_display = ('description', 'date_tarea', 'owner', 'state')
    list_filter = ('owner', 'state')
    search_fields = ['description',]

admin.site.register(Tareas, TareasAdmin)