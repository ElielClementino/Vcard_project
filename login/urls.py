from django.urls import path
from . import views

urlpatterns = {
    path('login/',views.user_register),
    path('profile/',views.profile),
}   

 # path('cadastra/', views.cadastra, name='cadastrar') # path('api/salvar_usuario',views.salvar_usuario, name = 'salvar_usuario')