from django.views.generic.edit import CreateView
from django.shortcuts import redirect, render
from django.contrib.auth import logout
from uservalidation.forms import FormUser
from django.urls import reverse_lazy


def user_login(request):
    return render(request, 'login/login.html')


def logout_view(request):
    logout(request)
    return redirect('/')


class CreateUser(CreateView):
    template_name = 'registrar/registrar_user.html'
    form_class = FormUser
    success_url = reverse_lazy('user.login')
