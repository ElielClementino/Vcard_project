"""vcard URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from . import views
from login import views



urlpatterns = [
    path('admin/', admin.site.urls),
<<<<<<< HEAD
    path('',views.introducao),
    path('',include('login.urls'))

=======
    path('apresentacao/', views.user_register),
    path('registrar/', views.user_register),
    path('profile/', views.profile),
>>>>>>> c20096502cfd2b2c82ab574de5ac2bb0c58a0399
]
