from django.shortcuts import render

def user_register(request):
    return render(request, 'login.html')

def profile(request):
    return render(request, 'vcard.html')
