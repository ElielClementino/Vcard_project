from django.urls import path
from . import views

urlpatterns = {
    path('',views.user_register, name = 'registrar_usuario'),
    path('cadastra/', views.cadastra, name='cadastrar')
    # path('api/salvar_usuario',views.salvar_usuario, name = 'salvar_usuario')
}