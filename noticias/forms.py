from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Submit
from django import forms
from django.core.validators import RegexValidator
from  django.forms import ModelForm

from noticias.models import Reportero, Noticia


class ReporteroForm(ModelForm):
    telefono = forms.CharField(
        max_length=10,
        validators = [
            RegexValidator(
            regex = '^[0-9]{10}$',
            message = 'Deben ser 10 numeros',
            code = 'Número de télefono invalido'
            )
        ],
        widget=forms.TextInput(attrs={'placeholder': 'Son 10 digítos'})
        #first_name = forms.CharField()
    )
    username = forms.CharField(
        label="Nombre de usuario",
        max_length=150,
        validators=[
            RegexValidator (
                regex= '[A-Za-z0-9\\@\\.\\+\\-\\_]+',
                message=('El usuario es invalido'),
                code = 'Usuario invalido'
            )
        ],
        widget=forms.TextInput(attrs={'placeholder': 'Letras, digitos y @,.,+,-,_'})
    )
    email = forms.EmailField()
    first_name = forms.CharField(
        label="Nombre/s",
        max_length=150,
        validators=[
            RegexValidator (
                regex='[A-Za-z]+(\\ [A-Za-z]+(\\ [A-Za-z]+)?)?',
                message=('El nombre es invalido'),
                code='Nombre invalido'
            )
        ]
    )
    last_name = forms.CharField(
        label="Apellidos",
        max_length=150,
        validators=[
            RegexValidator(
                regex='[A-Za-z]+(\\ [A-Za-z]+)?',
                message=('El apellido es invalido'),
                code='Apellido invalido'
            )
        ]
    )

    def __init__(self, *args, **kwargs):
        super(ReporteroForm,self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('username', css_class='form-group col-md-3'),
                 Column('password', css_class='form-group col-md-3')
            ),
            Row(
                Column('first_name',css_class='form-group col-md-3'),
                Column('last_name',css_class='form-group col-md-3'),
                Column('fecha_nacimiento', css_class='form-group col-md-3'),
                css_class="form-row"
            ),
            Row(
                Column('email', css_class='form-group col-md-4'),
                Column('telefono', css_class='form-group col-md-2')
            ),
            Row(
                Column('foto', css_class='form-group col-md-4'),
                Column('acta_nacimiento', css_class='form-group col-md-2')
            ),
            Submit('submit','Guardar')
        )

    class Meta:
        model = Reportero
        fields = ['username',
                  'password',
                  'first_name',
                  'last_name',
                  'email',
                  'telefono',
                  'fecha_nacimiento',
                  'foto',
                  'acta_nacimiento']
        widgets = {
            "password": forms.PasswordInput,
            "fecha_nacimiento": forms.DateInput(
                format="%Y-%m-%d",
                attrs={
                    'type': 'date',
                    'class': 'form-control',
                    'placeholder': 'seleccione una fecha'
                }
            ),
            "foto": forms.ClearableFileInput(attrs={'accept':'image/*'}),
            "acta_nacimiento": forms.ClearableFileInput(attrs={'accept':'pdf'}),
        }
        labels={
            "password":"Contraseña",
            "fecha_nacimiento":"Nacimiento"
        }


class NoticiaForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(NoticiaForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('titulo', css_class='form-group col-md-3'),
                 Column('fecha', css_class='form-group col-md-3')
            ),
            Row(
                Column('descripcion',css_class='form-group col-md-6')
                #css_class="form-row"
            ),
            Row(
                Column('reportero', css_class='form-group col-md-4'),
                Column('referencias', css_class='form-group col-md-2')
            ),
            Submit('submit','Guardar')
        )
    class Meta:
        model = Noticia
        fields = ['titulo',
                  'fecha',
                  'descripcion',
                  'reportero',
                  'referencias']
        widgets = {
            "titulo": forms.TextInput,
            "fecha": forms.DateInput(
                format="%Y-%m-%d",
                attrs={
                    'type': 'date',
                    'class': 'form-control',
                    'placeholder': 'seleccione una fecha'
                }
            ),
            "descripcion": forms.Textarea,
            "reportero": forms.TextInput,#ModelChoiceField(queryset=Reportero.objects.all())
            "referencias": forms.TextInput
        }
        labels = {
            "titulo": "Titulo",
            "fecha": "Fecha",
            "descripcion": "Contenido",
            "reportero": "Nombre del reportero",
            "referencias": "Referencia"
        }


