from django.db import models

# Create your models here.
class Equipo(models.Model):
    nombre = models.CharField(max_length=30)
    siglas = models.CharField(max_length=10)
    user_name_twitter = models.CharField(max_length=30)

    def __str__(self):
        return "%s - %s - %s" % (self.nombre, self.siglas, self.user_name_twitter)
    
class Jugador(models.Model):
    nombre = models.CharField(max_length=30)
    posicion = models.CharField(max_length=30)
    numero_camiseta = models.IntegerField()
    sueldo = models.IntegerField()
    equipo = models.ForeignKey(Equipo, related_name='jugadores', on_delete=models.CASCADE)

    def __str__(self):
        return "%s - %s - %d - %d - Equipo: %s" % (self.nombre, self.posicion, self.numero_camiseta, self.sueldo, self.equipo.nombre)

class Campeonato(models.Model):
    nombre = models.CharField(max_length=30)
    auspiciante = models.CharField(max_length=30)

    def __str__(self):
        return "%s - Auspiciante: %s" % (self.nombre, self.auspiciante)
    
class CampeonatoEquipos(models.Model):
    anio = models.IntegerField()
    campeonato = models.ForeignKey(Campeonato, related_name='campeonatosequipos', on_delete=models.CASCADE)
    equipo = models.ForeignKey(Equipo, related_name='campeonatosequipos', on_delete=models.CASCADE)

    def __str__(self):
        return "%d - %s - %s" % (self.anio, self.campeonato.nombre, self.equipo.nombre)
