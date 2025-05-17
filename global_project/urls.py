from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuario/', include('usuario.urls')),
from django.urls import path, re_path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cliente/', include('cliente.urls')),
    path('establecimiento/', include('establecimiento.urls')),
    path('reserva/', include('reserva.urls')),

    # Documentación automática:
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/docs/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
    path("api/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
    re_path("login/", views.login),
    re_path("register/", views.register),
    re_path("profile/", views.profile)
]