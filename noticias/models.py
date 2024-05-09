from datetime import date

from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Reportero(User, models.Model):
    telefono = models.CharField(max_length=10, blank=True)
    direccion = models.CharField(max_length=255)
    fecha_nacimiento = models.DateField(default='2000-01-01')
    foto = models.ImageField(upload_to='fotos/', blank=True)
    acta_nacimiento = models.FileField(upload_to='actas/', blank=True)
    # py manage.py makemigrations
    # None
    # py manage.py migrate
    # py manage.py createsuperuser
    # python -m pip install Pillow

    def get_edad(self):
        hoy = date.today()
        edad = hoy.year-self.fecha_nacimiento.year
        if (hoy.month, hoy.day) < (self.fecha_nacimiento.month, self.fecha_nacimiento.day):
            edad -= 1
        return edad

    def set_password(self, raw_password):
        self.password = make_password(raw_password)
        self._password = raw_password

class Noticia(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=255)
    fecha = models.DateField()
    descripcion = models.TextField()
    reportero = models.IntegerField()
    referencias = models.CharField(max_length=255)
    def get_reportero(self):
        reportero = Reportero.objects.filter(id=self.reportero).first()
        return reportero

