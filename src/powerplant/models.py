from django.db import models


class Fuels(models.Model):
    gas = models.FloatField(verbose_name="Gas (euro/MWh)")
    kerosine = models.FloatField(verbose_name="Kerosine (euro/MWh)")
    co2 = models.FloatField(verbose_name="CO2 (euro/ton)")
    wind = models.FloatField(verbose_name="Wind (%)")


class Powerplant(models.Model):
    PLANT_TYPE_CHOICES = [
        ('gasfired', 'Gas Fired'),
        ('turbojet', 'Turbojet'),
        ('windturbine', 'Wind Turbine'),
    ]

    name = models.CharField(max_length=100)
    type = models.CharField(max_length=20, choices=PLANT_TYPE_CHOICES)
    efficiency = models.FloatField()
    pmin = models.IntegerField()
    pmax = models.IntegerField()


class EnergyLoadRequest(models.Model):
    load = models.FloatField()
    fuels = models.OneToOneField(Fuels, on_delete=models.CASCADE)
    powerplants = models.ManyToManyField(Powerplant)
