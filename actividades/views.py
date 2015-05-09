from django.shortcuts import render
from django.db import models
from django.template.loader import get_template
from django.http import HttpResponse
from django.shortcuts import render_to_response
from actividades.models import *
from tarea.models import *


def lista(request, id):
	q_actividades = Actividades.objects.filter(tarea=id)
	actividades_template = 'lista_actividades.html'
	tarea_t = Tareas.objects.get(id=id)
	return render_to_response(actividades_template, locals())
