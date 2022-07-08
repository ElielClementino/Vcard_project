from django.shortcuts import render

def apresentacao(request):
    return render(request, 'introducao.html')
    
def user_register(request):
    return render(request, 'login.html')

def profile(request):
<<<<<<< HEAD
    return render(request,'Vcard.html')
=======
    return render(request, 'vcard.html')


>>>>>>> c20096502cfd2b2c82ab574de5ac2bb0c58a0399
