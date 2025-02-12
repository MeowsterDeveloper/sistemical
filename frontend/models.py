from django.db import models

class Contacto(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    codigo_area = models.CharField(max_length=5)
    telefono = models.CharField(max_length=8)
    email = models.EmailField(max_length=100)
    asunto = models.CharField(max_length=100)
    mensaje = models.TextField(max_length=396)
    fecha_envio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.asunto}"
