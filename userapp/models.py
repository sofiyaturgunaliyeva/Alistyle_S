from django.db import models
from django.contrib.auth.models import User


class Accaunt(models.Model):
    tanlov = [
        ("Erkak", "Erkak"),
        ("Ayol", "Ayol")
    ]
    jins = models.CharField(max_length=50 , choices=tanlov)
    shahar= models.CharField(max_length=30)
    davlat = models.CharField(max_length=30)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.davlat
