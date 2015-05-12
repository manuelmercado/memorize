from django.db import models
from django.contrib.auth.models import User
from tarea.models import Tareas


class Actividades(models.Model):
	fecha = models.DateTimeField(auto_now_add=True)
	tarea = models.ForeignKey(Tareas)
	Descripcion = models.TextField(blank=False)
	usuario = models.ForeignKey(User)

	def __unicode__(self):
		return self.Descripcion