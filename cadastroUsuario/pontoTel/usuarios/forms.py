from django.forms import ModelForm, fields
from .models import Person

class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = ['nome','email','endereco','pais','estado','municipio','cep','rua',
        'numero','complemento','cpf','pis','senha','foto']