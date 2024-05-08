from django.urls import path
from usuarios.views import LogoutSesion, GrupoAlta, GrupoListar, GrupoBaja, GrupoEdit, PermisoListar

urlpatterns = [
    path('logout', LogoutSesion.as_view(), name='logout'),
    path('grupo_listar', GrupoListar.as_view(), name='grupo_listar'),
    path('grupo_alta', GrupoAlta.as_view(), name='grupo_alta'),
    path('grupo_baja/<id>', GrupoBaja.as_view(),name='grupo_baja'),
    path('grupo_editar/<id>', GrupoEdit.as_view(),name='grupo_editar'),
    path('permiso_listar', PermisoListar.as_view(),name='permiso_listar'),
    ]
