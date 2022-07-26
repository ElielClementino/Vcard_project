from django import views
from django.urls import path
from django.contrib.auth import views as auth_views
from .views import CreateUser
from . import views


urlpatterns = [
    path('user_login/',auth_views.LoginView.as_view(template_name='login/login.html'), name='user.login'),
    path('logout', views.logout_view, name='logout'),
    path('user_register/', CreateUser.as_view(), name='user.register'),
]