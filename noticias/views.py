from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.views import View
from . models import Reportero
from noticias.forms import ReporteroForm
# Create your views here.


class Home(View):
    def get(self, request):
        cdx = {
            'titulo': 'Inicio',
            'encabezado': 'Periodico el mitotero',
            'hay_agregar': False,
        }
        return render(request, 'home/index.html', cdx)


class ReporteroView(View):
    def get(self, request):
        reporteros = Reportero.objects.all()
        cdx = {
            'titulo': 'Reportero',
            'reporteros': reporteros,
            'encabezado': 'Reporteros',
            'hay_agregar': True,
            'filtro': True,
            'link_agregar': "/reportero_alta",
            'btn_submit_texto': "Filtrar",
            'nombre': "nombre",
        }
        return render(request, 'reportero/listar.html', cdx)

    def post(self, request):
        reporteros = Reportero.objects.all()
        if 'filtro_checkbox' not in request.POST:
            nombre = request.POST['filtro']
            reporteros = Reportero.objects.filter(nombre__icontains=nombre).all()
        cdx = {
            'titulo': 'Reportero',
            'reporteros': reporteros,
            'encabezado': 'Reporteros',
            'hay_agregar': True,
            'filtro': True,
            'link_agregar': "/reportero_alta",
            'btn_submit_texto': "Filtrar",
            'nombre': "nombre",
        }
        return render(request, 'reportero/listar.html', cdx)


class ReporteroAlta(View):
    def get(self, request):
        formulario = ReporteroForm()
        cdx = {
            'titulo': 'Alta reporteros',
            'form': formulario,
            'encabezado': 'Alta de reporteros',
            'color_fondo': 'w3-green',
            'btn_submit_texto': "Guardar",
        }
        return render(request, 'reportero/abc.html', cdx)

    def post(self, request):
        form = ReporteroForm(request.POST, request.FILES, request)
        if form.is_valid():
            print(form.cleaned_data)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            form.save()
            user = Reportero.objects.filter(username=username).first()
            user.set_password(password)
            user.save()
            return redirect('reporteros')
        cdx = {
            'titulo': 'Alta Reporteros Error',
            'form': form,
            'encabezado': 'Alta de reporteros',
            'color_fondo': 'w3-green',
            'btn_submit_texto': "Guardar",
        }
        return render(request, 'reportero/abc.html', cdx)


class ReporteroBaja(View):
    def get(self, request, id):
        #Reportero.objects.filter(id=id).delete()
        reportero = Reportero.objects.filter(id=id).first()
        formulario = ReporteroForm(instance=reportero)
        cdx = {
            'titulo': 'Eliminar reportero',
            'encabezado': 'Eliminar reportero',
            'form': formulario,
            'color_fondo': 'w3-red',
            'btn_submit_texto' : "Eliminar"
        }
        return render(request,'reportero/abc.html',cdx)
    def post (self,request,id):
        Reportero.objects.filter(id=id).delete()
        return redirect('reporteros')

class ReporteroEdit(View):
    def get(self, request,id):
        reportero = Reportero.objects.filter(id=id).first()
        formulario = ReporteroForm(instance=reportero)
        cdx = {
            'titulo': 'Editar reportero',
            'encabezado': 'Editar reportero',
            'form': formulario,
            'color_fondo': 'w3-yellow',
            'btn_submit_texto' : "Guardar cambios",
        }
        return render(request,'reportero/abc.html',cdx)
    def post (self,request,id):
        reportero = Reportero.objects.filter(id=id).first()
        form = ReporteroForm(request.POST, request.FILES, instance=reportero)
        if form.is_valid():
            #print(f'password{form.cleaned_data["password"]}')
            form.save()
            reportero.set_password(form.cleaned_data["password"])
            reportero.save()
            return redirect('reporteros')
        cdx = {
            'titulo': 'Error al editar reportero',
            'form': form
        }
        return render(request, 'reportero/abc.html', cdx)
