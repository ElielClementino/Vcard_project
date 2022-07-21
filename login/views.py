from operator import contains
import sys
from django.shortcuts import render
from login.forms import Formulario
import os
from django.http import HttpResponse


def user_register(request):
    if request.method == "GET":
        form = Formulario()
        return render(request, 'formvalidation.html',{'form':form})
    else:
        form = Formulario(request.POST)
        nome = form.data['nome']
        sobrenome = form.data['sobrenome']
        profissao = form.data['profissao']
        email = form.data['email']
        telefone = form.data['telefone']

        vcf = gerar_vcard(nome, sobrenome,profissao ,email, telefone)

        with open(vcf, 'rb') as fh:
            #response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response = HttpResponse(fh.read(), content_type="application/text")  #file 
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(vcf)
            # response['Content-Disposition'] = 'inline; filename=' + os.path.basename(vcf)
            return response



def profile(request):
    return render(request, 'formvalidation.html')

def gerar_vcard(nome, sobrenome, profissao, email, telefone):
    original_stdout = sys.stdout
    output = print(f""" 
        Begin: VCARD
        Version: 1.0
        FullName: {nome} {sobrenome}
        Profission: {profissao}
        Email: {email}
        PhoneNumber: {telefone}
        End: My VCARD by {nome} {sobrenome}
        """)
    print(output)
    contact_file = './login/templates/contact.vcf'
    with open(contact_file, 'w') as download:
        download.writelines(f""" 
        Begin: VCARD
        Version: 1.0
        FullName: {nome} {sobrenome}
        Profission: {profissao}
        Email: {email}
        PhoneNumber: {telefone}
        End: My VCARD by {nome} {sobrenome}
        """)

    return contact_file


        # sys.stdout = download
        # sys.stdout = original_stdout



"""
2) Gerar um arquivo nome_completo.VCF (pesquisar como gerar arquivo txt em python)

3) Pequisar como retornar um File no Django para o frontend fazer download
"""