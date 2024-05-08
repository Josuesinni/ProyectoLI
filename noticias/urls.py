from django.urls import path
from noticias.views import Home, ReporteroView, ReporteroAlta, ReporteroBaja,ReporteroEdit

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('reportero',ReporteroView.as_view(), name='reporteros'),
    path('reportero_alta', ReporteroAlta.as_view(), name='reportero_alta'),
    path('reportero_baja/<id>', ReporteroBaja.as_view(), name='reportero_baja'),
    path('reportero_editar/<id>', ReporteroEdit.as_view(), name='reportero_editar'),
    ]