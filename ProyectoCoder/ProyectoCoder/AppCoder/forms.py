from django import forms


class EstadioFormulario(forms.Form):

    # Especificar los campos
    direccion = forms.CharField(required=True)
    anioFund = forms.IntegerField()
