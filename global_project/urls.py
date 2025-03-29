from django.contrib import admin
from django.urls import path, re_path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cliente/', include('cliente.urls')),
    path('establecimiento/', include('establecimiento.urls')),
    path('reserva/', include('reserva.urls')),

    re_path("login/", views.login),
    re_path("register/", views.register),
    re_path("profile/", views.profile)
]