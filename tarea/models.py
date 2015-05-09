from django.db import models

from usuario.models import Usuarios

class Tareas(models.Model):
	description = models.CharField(max_length=200)
	date_tarea = models.DateTimeField(auto_now=True)
	owner = models.ForeignKey(Usuarios)
	state = models.BooleanField()

	def __unicode__(self):
		return self.description