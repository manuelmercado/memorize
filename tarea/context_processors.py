from .models import *
from actividades.models import *
from django.utils.timezone import utc
from datetime import datetime, timedelta

def tsa(request):
	now = datetime.utcnow().replace(tzinfo=utc)
	p_tareas = Tareas.objects.filter(state=False)
	ids_tarea = []
	for i in p_tareas:
		p_actividades = Actividades.objects.filter(tarea=i.pk)
		if p_actividades:
			ultimo = p_actividades.latest('fecha')
			dias = now - ultimo.fecha
			ddias = dias.days
		else:
			ddias = 4

		if ddias > 3:
			ids_tarea.append(i.pk)

	return {'ids_tarea': len(ids_tarea)}