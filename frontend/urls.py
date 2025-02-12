from django.urls import path
from .views import index, enviar_formulario, about

urlpatterns = [
  path('', index, name='index'),
  path("contact?", enviar_formulario, name="contacto"),
  path('about?', about, name='about'),
  path('testing?', about, name='about'),
]