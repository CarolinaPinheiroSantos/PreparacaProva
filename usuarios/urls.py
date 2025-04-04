from django.urls import path
from . import views

urlpatterns = [
    path('auth/registro/', view=views.criar_usuario),
    path('auth/login/', view=views.logar_usuario_token)
]