from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.user_register, name='receber'),
    path('profile/',views.profile),
]
