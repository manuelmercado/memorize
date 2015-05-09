from django.db import models

class Usuarios(models.Model):
	usuario = models.CharField(max_length=20)
	nombre = models.CharField(max_length=50)
	email = models.EmailField(max_length=75)
	user_pass = models.CharField(max_length=20)

	def __unicode__(self):
		return self.usuario
