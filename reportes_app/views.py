# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import json

from django.utils.timezone import now
from django.utils.translation import ugettext as _
from django.views.generic import FormView
from django.http import HttpResponse

from ominicontacto_app.utiles import datetime_hora_minima_dia, UnicodeWriter

from reportes_app.forms import ReporteLlamadasForm, ExportarReporteLlamadasForm
from reportes_app.reporte_llamadas import ReporteDeLlamadas, GeneradorReportesLlamadasCSV


class ReporteLlamadasFormView(FormView):
    """Vista que despliega reporte de las grabaciones de las llamadas"""
    template_name = 'reporte_llamadas.html'
    form_class = ReporteLlamadasForm

    def get_initial(self):
        initial = super(ReporteLlamadasFormView, self).get_initial()
        hoy = now().date().strftime('%d/%m/%Y')
        initial['fecha'] = ' - '.join([hoy] * 2)
        return initial

    def get(self, request, *args, **kwargs):
        hoy_ahora = now()
        hoy_inicio = datetime_hora_minima_dia(hoy_ahora)
        reporte = ReporteDeLlamadas(hoy_inicio, hoy_ahora, False, request.user)
        estadisticas = reporte.estadisticas
        graficos = reporte.graficos
        return self.render_to_response(self.get_context_data(
            desde=hoy_inicio,
            hasta=hoy_ahora,
            estadisticas=estadisticas,
            graficos=graficos,
            estadisticas_json=json.dumps(estadisticas)))

    def form_valid(self, form):
        desde = form.desde
        hasta = form.hasta
        finalizadas = form.cleaned_data['finalizadas']
        reporte = ReporteDeLlamadas(desde, hasta, finalizadas, self.request.user)
        estadisticas = reporte.estadisticas
        graficos = reporte.graficos
        return self.render_to_response(self.get_context_data(
            desde=desde,
            hasta=hasta,
            estadisticas=estadisticas,
            graficos=graficos,
            estadisticas_json=json.dumps(estadisticas)))


class ExportarReporteLlamadasFormView(FormView):
    form_class = ExportarReporteLlamadasForm

    def form_valid(self, form):
        response = HttpResponse(content_type='text/csv')
        estadisticas = form.cleaned_data.get('estadisticas')
        tipo_reporte = form.cleaned_data.get('tipo_reporte')

        response['Content-Disposition'] = 'attachment; filename="{0}.csv"'.format(tipo_reporte)
        writer = UnicodeWriter(response)

        generador = GeneradorReportesLlamadasCSV()
        filas_csv = generador.obtener_filas_reporte(estadisticas, tipo_reporte)
        print filas_csv
        writer.writerows(filas_csv)
        # writer.writerow(REPORTE_SIN_DATOS)

        return response
