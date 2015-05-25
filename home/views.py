from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.db import models
from django.template.loader import get_template
from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response
from tarea.models import *
from django.utils.importlib import import_module
from django.conf import settings

@login_required(login_url="/singin")
def home(request):
	q_tareas=Tareas.objects.filter(state=False)
	if not q_tareas:
		raise Http404("No Existen Tareas Pendientes")
	home_template = 'home.html'
	return render_to_response(home_template, locals())