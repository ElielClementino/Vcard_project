from django.shortcuts import render

def apresentacao(request):
    return render(request, 'introducao.html')
    
def user_register(request):
    return render(request, 'login.html')

def profile(request):
    return render(request, 'vcard.html')


