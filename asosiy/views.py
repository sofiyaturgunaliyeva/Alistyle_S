from django.shortcuts import render
from django.views import View
from .models import *

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
        content = {
            "mahsulot": Mahsulot.objects.get(id = pk)
        }
        return render(request,'page-detail-product.html',content)