from django.urls import path
from . import views

urlpatterns = {
<<<<<<< HEAD
    path('login/',views.user_register),
    path('profile/',views.profile),
}   

 # path('cadastra/', views.cadastra, name='cadastrar') # path('api/salvar_usuario',views.salvar_usuario, name = 'salvar_usuario')
=======
    path('',views.user_register, name = 'registrar_usuario'),
    path('', views.profile, name='perfil_usuario' ),
    path('apresentacao/', views.apresentacao, name='apresentacao_site' ),
    # path('cadastra/', views.cadastra, name='cadastrar')
    # path('api/salvar_usuario',views.salvar_usuario, name = 'salvar_usuario')
}
>>>>>>> c20096502cfd2b2c82ab574de5ac2bb0c58a0399
