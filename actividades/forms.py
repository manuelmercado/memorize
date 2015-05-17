from django import forms
from django.forms import ModelForm
from .models import *

class add_actividadesForm(ModelForm):
	class Meta:
		model = Actividades
		fields = {'Descripcion'}