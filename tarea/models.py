from django.db import models

class Tarea(models.Model):
	description = models.CharField(max_length=200);
	date_tarea = models.DateTimeField(auto_now=True);
	
