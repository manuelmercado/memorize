from django.db import models

class Actividades(models.Model)
	fecha = models.DateTimeField(auto_now_add=True)
	tarea = models.ForeignKey('Tarea')
	Descripcion = models.TextField()
	usuario = models.ForeignKey('Usuario.usuario')



