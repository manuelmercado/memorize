from django import forms
from django.forms import ModelForm
from models import *

class TareaForm(ModelForm):
	class Meta:
		model = Tarea
	