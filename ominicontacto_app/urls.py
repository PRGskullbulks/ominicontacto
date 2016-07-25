
from django.conf.urls import url, patterns
from ominicontacto_app import (
    views, views_queue, views_base_de_datos_contacto, views_contacto)
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^ajax/mensaje_recibidos/',
        views.mensajes_recibidos_view,
        name='ajax_mensaje_recibidos'),
    url(r'^$', views.index_view, name='index'),
    url(r'^$', 'ominicontacto_app.views.index_view', name='index'),
    url(r'^accounts/login/$', views.login_view, name='login'),
    url(r'^user/nuevo/$',
        login_required(views.CustomerUserCreateView.as_view()),
        name='user_nuevo',
        ),
    url(r'^user/delete/(?P<pk>\d+)/$',
        login_required(views.UserDeleteView.as_view()),
        name='user_delete',
        ),
    url(r'^user/list/$', login_required(views.UserListView.as_view()),
        name='user_list',
        ),
    url(r'^user/update/(?P<pk>\d+)/$',
        login_required(views.CustomerUserUpdateView.as_view()),
        name='user_update',
        ),
    url(r'^user/agenteprofile/nuevo/(?P<pk_user>\d+)/$',
        login_required(views.AgenteProfileCreateView.as_view()),
        name='agenteprofile_nuevo',
        ),
    url(r'^modulo/nuevo/$',
        login_required(views.ModuloCreateView.as_view()), name='modulo_nuevo',
        ),
    url(r'^modulo/list/$',
        login_required(views.ModuloListView.as_view()), name='modulo_list',
        ),
    url(r'^agente/list/$',
        login_required(views.AgenteListView.as_view()), name='agente_list',
        ),
    url(r'^user/agenteprofile/update/(?P<pk_agenteprofile>\d+)/$',
        login_required(views.AgenteProfileUpdateView.as_view()),
        name='agenteprofile_update',
        ),
    url(r'^grupo/nuevo/$',
        login_required(views.GrupoCreateView.as_view()), name='grupo_nuevo',
        ),
    url(r'^grupo/update/(?P<pk>\d+)/$',
        login_required(views.GrupoUpdateView.as_view()),
        name='grupo_update',
        ),
    url(r'^grupo/list/$',
        login_required(views.GrupoListView.as_view()), name='grupo_list',
        ),
    url(r'^queue/nuevo/$',
        login_required(views_queue.QueueCreateView.as_view()),
        name='queue_nuevo',
        ),
    url(r'^queue_member/(?P<pk_queue>[\w\-]+)/$',
        login_required(views_queue.QueueMemberCreateView.as_view()),
        name='queue_member',
        ),
    url(r'queue/list/$',
        login_required(views_queue.QueueListView.as_view()),
        name='queue_list',
        ),
    url(r'^queue/elimina/(?P<pk_queue>[\w\-]+)/$',
        login_required(views_queue.QueueDeleteView.as_view()),
        name='queue_elimina',
        ),
    url(r'^queue/update/(?P<pk_queue>[\w\-]+)/$',
        login_required(views_queue.QueueUpdateView.as_view()),
        name='queue_update',
        ),
    url(r'^queue_member/(?P<pk_queuemember>\d+)/elimina/(?P<pk_queue>[\w\-]+)/$',
        login_required(views_queue.queue_member_delete_view),
        name='queuemember_elimina',
        ),
    url(r'^pausa/nuevo/$',
        login_required(views.PausaCreateView.as_view()),
        name='pausa_nuevo',
        ),
    url(r'^pausa/list/$',
        login_required(views.PausaListView.as_view()),
        name='pausa_list',
        ),
    url(r'^node/$', login_required(views.node_view), name='view_node'),
    url(r'^smsThread/$',
        login_required(views.mensajes_recibidos_enviado_remitente_view),
        name='view_sms_thread'),
    url(r'^sms/getAll/$',
        login_required(views.mensajes_recibidos_view),
        name='view_sms_get_all'),
    url(r'^blanco/$',
        login_required(views.blanco_view),
        name='view_blanco'),
    # ==========================================================================
    # Base Datos Contacto
    # ==========================================================================
    url(r'^base_datos_contacto/nueva/$',
        login_required(views_base_de_datos_contacto.
                       BaseDatosContactoCreateView.as_view()),
        name='nueva_base_datos_contacto'
        ),
    url(r'^base_datos_contacto/(?P<pk>\d+)/validacion/$',
        login_required(views_base_de_datos_contacto.
                       DefineBaseDatosContactoView.as_view()),
        name='define_base_datos_contacto',
        ),
    url(r'^base_datos_contacto/$',
        login_required(views_base_de_datos_contacto.
                       BaseDatosContactoListView.as_view()),
        name='lista_base_datos_contacto',
        ),
    url(r'^contacto/nuevo/$',
        login_required(views_contacto.ContactoCreateView.as_view()),
        name='contacto_nuevo',
        ),
    url(r'^contacto/list/(?P<pagina>\d+)/$',
        login_required(views_contacto.ContactoListView.as_view()),
        name='contacto_list',
        ),
    url(r'^contacto/(?P<id_cliente>\d+)/update/$',
        login_required(views_contacto.ContactoUpdateView.as_view()),
        name='contacto_update',
        ),
    url(r'^contacto/(?P<telefono>[\w\-]+)/list/$',
        login_required(views_contacto.ContactoTelefonoListView.as_view()),
        name='contacto_list_telefono',
        ),
    url(r'^contacto/buscar/$',
        login_required(views_contacto.BusquedaContactoFormView.as_view()),
        name='contacto_buscar',
        ),
]
