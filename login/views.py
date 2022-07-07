from django.shortcuts import render

def user_register(request):
    return render(request, 'login.html')

def cadastra(request):
    return render(request, 'cadastra.html')
