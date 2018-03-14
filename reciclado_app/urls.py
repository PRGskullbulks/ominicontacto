# -*- coding: utf-8 -*-

from django.conf import settings
from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from reciclado_app import views

urlpatterns = [
        url(r'^reciclar/(?P<pk_campana>\d+)/dialer/$',
            login_required(views.ReciclarCampanaDialerFormView.as_view()),
            name='reciclar_campana_dialer'),
]