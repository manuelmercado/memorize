from django.db import models

from tarea.models import Tareas
from usuario.models import Usuarios

class Actividades(models.Model):
	fecha = models.DateTimeField(auto_now_add=True)
	tarea = models.ForeignKey(Tareas)
	Descripcion = models.TextField(blank=False)
	usuario = models.ForeignKey(Usuarios)



