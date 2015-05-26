from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.http import HttpResponseRedirect
from django.utils.timezone import utc
from datetime import datetime, timedelta
from forms import *
from actividades.models import *
from .models import *

def add_tarea(request):
	if request.method == "POST":
		form = TareaForm(request.POST)
		if form.is_valid():
			tarea = form.save(commit=False)
			tarea.state = False
			tarea.owner = request.user
			tarea.save()
			return HttpResponseRedirect('/actividades/add_actividades/id=%s' % tarea.id)
	else:
		form = TareaForm()
	return render_to_response('tarea_add.html', context_instance = RequestContext(request, locals()))

def tarea_sin_atencion(request):
	now = datetime.utcnow().replace(tzinfo=utc)
	p_tareas = Tareas.objects.filter(state=False)
	pks_tarea = []
	for i in p_tareas:
		p_actividades = Actividades.objects.filter(tarea=i.pk)
		if p_actividades:
			ultimo = p_actividades.latest('fecha')
			dias = now - ultimo.fecha
			ddias = dias.days
		else:
			ddias = 4

		if ddias > 3:
			pks_tarea.append(i.pk)
	tareas_sa = Tareas.objects.filter(pk__in=pks_tarea)
	return render_to_response('tarea_p.html',locals())

