from django import forms
import datetime


class JugadorFormulario(forms.Form):

    # Especificar los campos
    apellido = forms.CharField()
    numero = forms.IntegerField()
    esBueno = forms.BooleanField()


class EmpleadoFormulario(forms.Form):

    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    dni = forms.IntegerField()
    profesional = forms.BooleanField()
    fechaDeNacimiento = forms.DateField(initial=datetime.date.today)


class EstadioFormulario(forms.Form):

    # Especificar los campos
    direccion = forms.CharField(required=True)
    anioFund = forms.IntegerField()
