
from django.conf.urls import url, patterns
# from ominicontacto_app import views

urlpatterns = patterns('',
    url(r'^ajax/mensaje_recibidos/',
        'ominicontacto_app.views.mensajes_recibidos_view',
        name='ajax_mensaje_recibidos'),
    url(r'^$', 'ominicontacto_app.views.index_view', name='index'),
)
