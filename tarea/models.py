from django.db import models

class Tarea(models.Model):
	id_tarea = models.CharField(max_length=20)
	description = models.CharField(max_length=200)
	date_tarea = models.DateTimeField(auto_now=True)
	owner = models.ForeignKey('Usuario.usuario')
	state = models.BooleanField()

	
