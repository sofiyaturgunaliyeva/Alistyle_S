from django.db import models
from userapp.models import Accaunt
from asosiy.models import Mahsulot

class Tanlangan(models.Model):
    mahsulot = models.ForeignKey(Mahsulot,on_delete=models.CASCADE)
    accaunt = models.ForeignKey(Accaunt,on_delete=models.CASCADE)

    def __str__(self):
        return self.mahsulot.nom


class Savat(models.Model):
    tanlov = [
        ("buyurtma qlindi","buyurtma qlindi"),
        ("buyurtma qlinmadi","buyurtma qlinmadi")
    ]
    accaunt = models.ForeignKey(Accaunt, on_delete=models.CASCADE)
    umumiy_summa = models.IntegerField()
    sana = models.DateField(auto_now_add=True)
    holat = models.CharField(max_length=30,choices=tanlov)

    # def save(self, *args, **kwargs):
    #     savat_items = SavatItem.objects.filter(savat__id = self.id)
    #     summa = 0
    #     for item in savat_items:
    #         ch = (item.mahsulot.narx/100)*item.mahsulot.chegirma
    #         narxi = self.ma


class SavatItem(models.Model):
    savat = models.ForeignKey(Savat, on_delete=models.CASCADE)
    mahsulot = models.ForeignKey(Mahsulot, on_delete=models.CASCADE)
    miqdor = models.PositiveSmallIntegerField()
    summa = models.PositiveSmallIntegerField()

    # def save(self, *args, **kwargs):
    #     ch = (self.mahsulot.narx / 100) * self.mahsulot.chegirma
    #     narxi = self.mahsulot.narx - int(ch)
    #     self.summa = narxi * self.miqdor
    #     super(SavatItem,self)
    #

    def __str__(self):
        return self.mahsulot.nom

