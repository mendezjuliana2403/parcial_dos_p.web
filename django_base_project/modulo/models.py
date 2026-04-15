from django.db import models
from django.contrib.auth.models import User

class Comida(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    pais = models.CharField(max_length=100)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    imagen = models.ImageField(upload_to='comidas/', null=True, blank=True)

    # Campos adicionales según contexto
    ingredientes = models.TextField()
    nivel_dificultad = models.CharField(max_length=50)

    creado_por = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo
