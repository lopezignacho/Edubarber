from django.db import models

# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    contraseña = models.CharField(max_length=30)
    
    def __str__(self):
        return self.nombre
