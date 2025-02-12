from django.contrib import admin
from .models import Contacto  # Importa el modelo que quieres ver en el admin

# Registrar el modelo en el admin
admin.site.register(Contacto)
