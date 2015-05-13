from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.db import models
from django.template.loader import get_template
from django.http import HttpResponse
from django.shortcuts import render_to_response
from tarea.models import *
from django.utils.importlib import import_module
from django.conf import settings

@login_required(login_url="/singin")
def home(request):
	q_tareas=Tareas.objects.filter(state=False)
	home_template = 'home.html'
	return render_to_response(home_template, locals())