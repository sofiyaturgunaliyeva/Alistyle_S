from django.shortcuts import render,redirect
from django.views import View
from .models import *
from userapp.models import Accaunt
from django.db.models import *

# Vazifa

# 1- Buyurtma appda page-profile-wishlist.htmlni qaytaruvchi view yozing. headers.htmlni bog’lang.
# Hozirgi akkauntga tegishli hamma tanlanganlar shu sahifada ko’rinsin.

class HammaTanlanganlarView(View):
    def get(self,request):
        content = {
            "tanlanganlar": Tanlangan.objects.filter(accaunt__user = request.user)
        }
        return render(request,'page-profile-wishlist.html',content)

# 2.  page-shopping-cart.html’ni qaytaruvchi view yozing.

class ShoppingView(View):
    def get(self,request):
        savati = Savat.objects.get(accaunt__user = request.user)
        itemlar = SavatItem.objects.filter(savat=savati)
        narx_sum = 0
        ch = 0
        for item in itemlar:
            ch += ((item.mahsulot.narx / 100) * item.mahsulot.chegirma)* item.miqdor
            narx_sum += item.mahsulot.narx * item.miqdor
        savati.umumiy_summa = narx_sum - ch
        savati.save()
        content = {
            "savat":savati,
            "itemlar": itemlar,
            "total": narx_sum,
            "discount": ch,
            "price": narx_sum - ch

        }
        return render(request,'page-shopping-cart.html',content)

# 3. page-profile-orders.html’ni qaytaruvchi view yozing.

class ProfileView(View):
    def get(self,request):
        return render(request,'page-profile-orders.html')


# 4. Bironta tanlangan obyektni o’chirib yuboruvchi view yozing.

class TanlanganOchirView(View):
    def get(self,request,pk):
        Tanlangan.objects.get(mahsulot__id =pk).delete()
        return redirect('tanlanganlar')


class MiqdorKamaytir(View):
    def get(self,request,pk):
        item = SavatItem.objects.get(id = pk)
        if item.miqdor > 1:
            item.miqdor -= 1
            item.summa -= item.mahsulot.narx
            item.save()
        return redirect('/buyurtma/shopping/')


class MiqdorQosh(View):
    def get(self, request, pk):
        item = SavatItem.objects.get(id=pk)
        item.miqdor += 1
        item.summa += item.mahsulot.narx
        item.save()
        return redirect('/buyurtma/shopping/')

class SavatItemQosh(View):
    def get(self,request,pk):
        savati = Savat.objects.get(account__user = request.user)
        m = Mahsulot.objects.get(id = pk)
        savat_item = SavatItem.objects.filter(mahsulot = m, savat = savati)
        if len(savat_item) == 0:
            return redirect('/buyurtma/shopping/')

        SavatItem.objects.create(
            miqdor = 1,
            mahsulot = m,
            savat = savati,
            summa = m.narx
        )
        return redirect(f"/asosiy/mahsulot")