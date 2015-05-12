from django.db import models
from django.contrib.auth.models import User

class Tareas(models.Model):
	description = models.CharField(max_length=200)
	date_tarea = models.DateTimeField(auto_now_add=True)
	owner = models.ForeignKey(User)
	state = models.BooleanField()

	def __unicode__(self):
		return self.description