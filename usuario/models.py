from django.db import models

class Usuario(models.Model):
	usuario = models.CharField(max_legth=20)
	nombre = models.CharField(max_legth=50)
	email = models.EmailField(max_legth=75)
	user_pass = model.CharField(max_legth=20)
