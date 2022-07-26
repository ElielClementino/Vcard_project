from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.user_register, name='receber.dados'),
    path('profile/', views.profile, name='user.profile'),
]
