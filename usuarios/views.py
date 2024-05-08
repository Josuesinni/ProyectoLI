from django.contrib.auth import logout
from django.contrib.auth.models import Group, Permission, User
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import render, redirect
from django.views import View

from usuarios.forms import GroupForm


# Create your views here.
class LogoutSesion(View):
    def get(self, request):
        logout(request)  # Cierra la sesión del usuario actual
        return redirect('home')  # Redirige a la página de inicio o a otra página deseada


class GrupoListar(View):
    def get(self, request):
        grupos = Group.objects.all()
        cdx = {
            'grupos': grupos,
            'titulo': 'Grupos',
            'encabezado': "Grupos",
            'hay_agregar': True,
            'link_agregar': "/usuarios/grupo_alta",
        }
        return render(request, 'grupo_listar.html', cdx)


class GrupoAlta(View):
    def get(self, request):
        form = GroupForm()
        cdx = {
            'form': form,
            'titulo': 'Grupo Nuevo',
            'encabezado': "Grupo Nuevo",
        }
        return render(request, 'grupo_abc.html', cdx)

    def post(self, request):
        form = GroupForm(request.POST)
        # print(f'name: {form.clean_name()}')
        if form.is_valid():
            form.save()
            return redirect('grupo_listar')
        cdx = {
            'form': form,
            'titulo': 'Grupo Nuevo',
            'encabezado': "Grupo Nuevo",
        }
        return render(request, 'grupo_abc.html', cdx)


class GrupoBaja(View):
    def get(self, request, id):
        grupo = Group.objects.filter(id=id).first()
        formulario = GroupForm(instance=grupo)
        cdx = {
            'titulo': 'Eliminar grupo',
            'encabezado': 'Eliminar grupo',
            'form': formulario,
            'color_fondo': 'w3-red',
            'btn_submit_texto': "Eliminar"
        }
        return render(request, 'grupo_abc.html', cdx)

    def post(self, request, id):
        Group.objects.filter(id=id).delete()
        return redirect('grupo_listar')


class GrupoEdit(View):
    def get(self, request, id):
        grupo = Group.objects.filter(id=id).first()
        formulario = GroupForm(instance=grupo)
        cdx = {
            'titulo': 'Editar grupo',
            'encabezado': 'Editar grupo',
            'form': formulario,
            'color_fondo': 'w3-yellow',
            'btn_submit_texto': "Guardar cambios",
        }
        return render(request, 'grupo_abc.html', cdx)

    def post(self, request, id):
        grupo = Group.objects.filter(id=id).first()
        form = GroupForm(request.POST, instance=grupo)
        if form.is_valid():
            # print(f'password{form.cleaned_data["password"]}')
            form.save()
            return redirect('grupo_listar')
        cdx = {
            'titulo': 'Error al editar el grupo',
            'form': form
        }
        return render(request, 'grupo_abc.html', cdx)

class PermisoListar(View):
    def get(self, request):
        lista_app=[]
        lista_app.append(ContentType.objects.get_for_model(User))
        lista_app.append(ContentType.objects.get_for_model(Group))
        lista_app.append(ContentType.objects.get_for_model(Permission))
        permisos = Permission.objects.filter(content_type__in=lista_app).all()
        #permisos = Permission.objects.all()
        cdx = {
            'permisos': permisos,
            'titulo': 'Permisos',
            'encabezado': "Permisos",
            'hay_agregar': True,
            'link_agregar': "/usuarios/permiso_alta",
        }
        return render(request, 'permiso_listar.html', cdx)