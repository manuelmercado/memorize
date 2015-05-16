from django import forms
from django.forms import ModelForm
from tarea.models import *

class TareaForm(ModelForm):
	class Meta:
		model = Tareas
		fields = ['description']
		
	
