from django.shortcuts import render
from login.forms import Formulario
from django.http import HttpResponse


def user_register(request):
    if request.method == "GET":
        form = Formulario()
        return render(request, 'formvalidation.html', {'form': form})
    else:
        form = Formulario(request.POST)
        nome = form.data['nome']
        sobrenome = form.data['sobrenome']
        profissao = form.data['profissao']
        email = form.data['email']
        telefone = form.data['telefone']

        vcf = gerar_vcard(nome, sobrenome, profissao, email, telefone)
        return HttpResponse(vcf, content_type="application/text")


def profile(request):
    return render(request, 'formvalidation.html')


def gerar_vcard(nome, sobrenome, profissao, email, telefone):
    output = f"""
        Begin: VCARD
        Version: 1.0
        FullName: {nome} {sobrenome}
        Profission: {profissao}
        Email: {email}
        PhoneNumber: {telefone}
        End: My VCARD by {nome} {sobrenome}
        """
    return output
