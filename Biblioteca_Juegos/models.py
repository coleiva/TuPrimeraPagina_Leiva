from django.db import models

class JuegoPC(models.Model):
    nombre = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    lanzamiento = models.IntegerField()
    reseña = models.TextField()
    imagen = models.ImageField(upload_to='juegos_pc/', null=True, blank=True)
    consola = models.CharField(max_length=20, default='Juego PC')

    def __str__(self):
        return self.nombre

class JuegoNintendo(models.Model):
    nombre = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    lanzamiento = models.IntegerField()
    reseña = models.TextField()
    imagen = models.ImageField(upload_to='juegos_nintendo/', null=True, blank=True)
    consola = models.CharField(max_length=20, default='Juego Nintendo')

    def __str__(self):
        return self.nombre

class JuegoSony(models.Model):
    nombre = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    lanzamiento = models.IntegerField()
    reseña = models.TextField()
    imagen = models.ImageField(upload_to='juegos_sony/', null=True, blank=True)
    consola = models.CharField(max_length=20, default='Juego Sony')

    def __str__(self):
        return self.nombre