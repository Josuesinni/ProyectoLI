from django.urls import path
from noticias.views import Home, ReporteroView, ReporteroAlta, ReporteroBaja, ReporteroEdit, NoticiaView, NoticiaAlta, NoticiaBaja, NoticiaEdit
urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('reportero',ReporteroView.as_view(), name='reporteros'),
    path('reportero_alta', ReporteroAlta.as_view(), name='reportero_alta'),
    path('reportero_baja/<id>', ReporteroBaja.as_view(), name='reportero_baja'),
    path('reportero_editar/<id>', ReporteroEdit.as_view(), name='reportero_editar'),
    path('noticia', NoticiaView.as_view(), name='noticia'),
    path('noticia_alta', NoticiaAlta.as_view(), name='noticia_alta'),
    path('noticia_baja/<id>', NoticiaBaja.as_view(), name='noticia_baja'),
    path('noticia_editar/<id>', NoticiaEdit.as_view(), name='noticia_editar'),
    ]