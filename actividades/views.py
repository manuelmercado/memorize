from django.shortcuts import render
from django.db import models
from django.template.loader import get_template
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from actividades.models import *
from tarea.models import *
from .forms import *


def lista(request, id):
	q_actividades = Actividades.objects.filter(tarea=id)
	actividades_template = 'lista_actividades.html'
	tarea_t = Tareas.objects.get(id=id)
	return render_to_response(actividades_template, locals())

def add_actividades(request, id):
	idd = int(id)
	tarea_id = Tareas.objects.get(id=id)
	if request.method == "POST":
		form = add_actividadesForm(request.POST)
		if form.is_valid():
			actividades = form.save(commit=False)
			actividades.tarea = tarea_id
			actividades.usuario = request.user
			actividades.save()
			return HttpResponseRedirect('/actividades/id=%s' % idd)
	else:
		form = add_actividadesForm()
	return render_to_response('add_actividades.html', context_instance = RequestContext(request, locals()))	
