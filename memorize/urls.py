from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    url(r'^$', 'home.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^actividades/id=(\d+)$', 'actividades.views.lista', name='lista'),
    url(r'^singin/', 'user_p.views.login_user', name='login_user'),
    url(r'^logout_p/', 'user_p.views.logout_view', name='logout_view'),
    # url(r'^singin2/', 'user_p.views.login_view', name='login_view'),
]
