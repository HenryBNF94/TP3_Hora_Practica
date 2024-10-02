from django.db import models

# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    categoria = models.CharField(max_length=255)
    precio = models.FloatField()