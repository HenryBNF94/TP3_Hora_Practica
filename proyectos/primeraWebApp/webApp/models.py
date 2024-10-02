from django.db import models

# Create your models here.



class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    categoria = models.CharField(max_length=255)
    precio = models.FloatField()

    def __str__(self):
        return self.nombre + " | " + self.categoria 
    
class Marca(models.Model):
    nombre = models.CharField(max_length=255)
    pais = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre