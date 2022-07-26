from django import forms


class Formulario(forms.Form):
    nome = forms.CharField(max_length=30)
    sobrenome = forms.CharField(max_length=30)
    profissao = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=120)
    telefone = forms.CharField(max_length=15)
