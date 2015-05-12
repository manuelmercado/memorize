from django.shortcuts import render
from forms import *

def add(request):
	if request.method == "POST":
		form = TareaForm(request.POST)
		if form.is_valid():
			tarea = form.save(commit=False)
			tarea.owner = request.user
			tarea.save()
			return httpResponseRedirect('/')
		else:
			form = TareaForm()	

