from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    url(r'^$', 'tarea.views.tarea_sin_atencion', name='tarea_sin_atencion'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^actividades/id=(\d+)$', 'actividades.views.lista', name='lista'),
    url(r'^singin/', 'user_p.views.login_user', name='login_user'),
    url(r'^logout_p/', 'user_p.views.logout_view', name='logout_view'),
    url(r'^add_tarea/', 'tarea.views.add_tarea', name='add_tarea'),
    url(r'^tareas_pendientes', 'home.views.home', name='home'),
    url(r'^actividades/add_actividades/id=(\d+)$', 'actividades.views.add_actividades', name='add_actividades'),
    url(r'^tareas/tarea_sa/', 'tarea.views.tarea_sin_atencion', name='tarea_sin_atencion'),

]
