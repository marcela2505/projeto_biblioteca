from django import forms
from .models import Livro

class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = ["titulo", "autor", "ano_publicacao", "genero", "disponivel"]
        widgets = {
            "titulo": forms.TextInput(attrs={"class": "form-control"}),
             "autor": forms.TextInput(attrs={"class": "form-control"}), 
            "ano_publicacao": forms.NumberInput(attrs={"class": "form-control"}),
            "genero": forms.TextInput(attrs={"class": "form-control"}),
            "disponivel": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }
