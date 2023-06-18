from django.shortcuts import render,redirect
from django.views import View
from .models import *
from userapp.models import Accaunt
from django.db.models import *

class Home(View):
    def get(self,request):
        content = {
            "bolimlar":Bolim.objects.all()[:7]
        }
        return render(request,'page-index.html',content)

class HomeLoginsiz(View):
    def get(self,request):

        return render(request,'page-index-2.html')


 # Vazifa:
#
# 1. Bitta bo'limga tegishli hamma mahsulotlarni chiqaruvchi viewni oxiriga yetkazing.

class MahsulotlarView(View):
    def get(self,request,pk):
        content = {
            "mahsulotlar": Mahsulot.objects.filter(bolim__id = pk)
        }
        return render(request,'page-listing-grid.html',content)

#  page-category.html'ini ko'rsatuvchi view yozing ('bolimlar/'). headers.html'ni bog'lang.

class BolimlarView(View):
    def get(self,request):
        content = {
            'bolimlar':Bolim.objects.all()
        }
        return render(request, 'page-category.html',content)

class BittaMahsulotView(View):
    def get(self,request,pk):
        izohlar = Izoh.objects.filter(mahsulot__id = pk)
        ortachasi = izohlar.aggregate(Avg('baho')).get('baho__avg')
        content = {
            "mahsulot": Mahsulot.objects.get(id = pk),
            "izohlar": Izoh.objects.filter(mahsulot__id = pk),
            "izoh_soni":len(izohlar),
            "ortachasi": ortachasi * 20
        }
        return render(request,'page-detail-product.html',content)

    def post(self,request,pk):
        Izoh.objects.create(
            matn = request.POST.get('comment'),
            baho = request.POST.get('rating'),
            accaunt = Accaunt.objects.get(user=request.user),
            mahsulot = Mahsulot.objects.get(id=pk)
        )
        return redirect(f"/asosiy/mahsulot/{pk}/")