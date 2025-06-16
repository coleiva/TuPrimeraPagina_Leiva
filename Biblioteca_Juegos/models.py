from django.db import models

class JuegoPC(models.Model):
    nombre = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    lanzamiento = models.IntegerField()
    reseña = models.TextField()

    def __str__(self):
        return self.nombre

class JuegoNintendo(models.Model):
    nombre = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    lanzamiento = models.IntegerField()
    reseña = models.TextField()

    def __str__(self):
        return self.nombre

class JuegoSony(models.Model):
    nombre = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    lanzamiento = models.IntegerField()
    reseña = models.TextField()

    def __str__(self):
        return self.nombre