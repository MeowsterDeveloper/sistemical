from django.shortcuts import render, redirect
import requests
from .models import Contacto
from django.contrib import messages

def index(request):
  return render(request, 'index.html')

def enviar_formulario(request):
    if request.method == "POST":
        # Validar reCAPTCHA
        recaptcha_response = request.POST.get('g-recaptcha-response')
        recaptcha_secret = "6LenWdQqAAAAAIToJtuv7gDStD0IMh6-P5XRH859"
        recaptcha_verify_url = "https://www.google.com/recaptcha/api/siteverify"
        recaptcha_data = {
            "secret": recaptcha_secret,
            "response": recaptcha_response
        }
        recaptcha_result = requests.post(recaptcha_verify_url, data=recaptcha_data).json()

        if not recaptcha_result.get("success"):
            messages.error(request, "Verificación reCAPTCHA fallida. Inténtalo de nuevo.")
            return redirect("contacto")

        # Continuar con la validación de los otros campos
        nombre = request.POST.get("firstname", "").strip()
        apellido = request.POST.get("lastname", "").strip()
        codigo_area = request.POST.get("areacode", "").strip()
        telefono = request.POST.get("phone", "").strip()
        email = request.POST.get("age", "").strip()
        asunto = request.POST.get("address", "").strip()
        mensaje = request.POST.get("message", "").strip()

        if not all([nombre, apellido, codigo_area, telefono, email, asunto, mensaje]):
            messages.error(request, "Todos los campos son obligatorios.")
            return redirect("contacto")

        # Guardar en la base de datos
        Contacto.objects.create(
            nombre=nombre,
            apellido=apellido,
            codigo_area=codigo_area,
            telefono=telefono,
            email=email,
            asunto=asunto,
            mensaje=mensaje
        )

        messages.success(request, "Tu mensaje ha sido enviado correctamente.")
        return redirect("contacto")

    return render(request, "contact.html")

def about(request):
  return render(request, 'about.html')

def scripttest(request):
  return render(request, 'scripttest.html')