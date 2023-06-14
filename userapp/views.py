from django.shortcuts import render,redirect
from.models import *
from django.contrib.auth import authenticate, login, logout

from django.views import View



#  Vazifa

#  userappda page-user-register va page-user-login htmllarini ko'rsatuvchi viewlarni yozing.
#  Userapp o'zi uchun ham alohida urls.py faylini qo'shib oling.
# Ikkala htmlga ham headers.html'ni bog'lang.

# 1. RegisterView uchun post metodni qo'shing.
# Yangi foydalanuvchi sifatida ro'yhatdan o'tishda ham User, ham Account create qilinishi kerak.

class RegisterView(View):
    def get(self,request):
        return render(request,'page-user-register.html')

    def post(self,request):
        u = User.objects.create_user(
            username=request.POST.get('login'),
            password=request.POST.get('password')
        )
        Accaunt.objects.create(
            jins = request.POST.get('jins'),
            shahar = request.POST.get('shahar'),
            davlat = request.POST.get('davlat'),
            user=u
        )
        return redirect('login')







class LoginView(View):
    def get(self,request):
        return render(request,'page-user-login.html')

    def post(self,request):
        user = authenticate(  # bor bo'lsa userni , yo'q bo'lsa None
            username=request.POST.get('login'),
            password=request.POST.get('parol')
        )
        if user is None:
            return redirect("login")
        login(request, user)
        return redirect("home")


class LogoutView(View):
    def get(self,request):
        logout(request)
        return redirect("login")








