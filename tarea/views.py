from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.http import HttpResponseRedirect

from forms import *

def add_tarea(request):
	if request.method == "POST":
		form = TareaForm(request.POST)
		if form.is_valid():
			tarea = form.save(commit=False)
			tarea.state = False
			tarea.owner = request.user
			tarea.save()
			return HttpResponseRedirect('/')
	else:
			form = TareaForm()
	return render_to_response('tarea_add.html', context_instance = RequestContext(request, locals()))