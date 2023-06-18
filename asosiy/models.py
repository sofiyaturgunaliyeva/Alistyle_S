from django.db import models
from userapp.models import Accaunt

class Bolim(models.Model):
    nom = models.CharField(max_length=100)
    rasm = models.FileField(upload_to='bolimlar')

    def __str__(self):
        return self.nom
class Mahsulot(models.Model):
    nom = models.CharField(max_length=100)
    narx = models.IntegerField()
    min_miqdor = models.SmallIntegerField(default=1)
    bolim = models.ForeignKey(Bolim,on_delete=models.CASCADE)
    davlat = models.CharField(max_length=100)
    brend = models.CharField(max_length=100)
    matn = models.TextField()
    kafolat = models.CharField(max_length=20)
    yetkazish = models.CharField(max_length=20)
    chegirma = models.PositiveSmallIntegerField(default=0)
    mavjud = models.BooleanField(default=True)

    def __str__(self):
        return self.nom

class Media(models.Model):
    rasm = models.FileField(upload_to='mahsulotlar')
    mahsulot = models.ForeignKey(Mahsulot, on_delete=models.CASCADE)

    def __str__(self):
        return self.mahsulot.nom

class Izoh(models.Model):
    matn = models.TextField()
    sana =  models.DateField(auto_now_add=True)
    baho = models.PositiveSmallIntegerField()
    mahsulot = models.ForeignKey(Mahsulot,on_delete=models.CASCADE)
    accaunt = models.ForeignKey(Accaunt,on_delete=models.CASCADE)

    def __str__(self):
        return self.matn

