from django.shortcuts import render
from.models import *
from django.contrib.auth import authenticate, login, logout

from django.views import View



#  Vazifa

#  userappda page-user-register va page-user-login htmllarini ko'rsatuvchi viewlarni yozing.
#  Userapp o'zi uchun ham alohida urls.py faylini qo'shib oling.
# Ikkala htmlga ham headers.html'ni bog'lang.

class RegisterView(View):
    def get(self,request):
        return render(request,'page-user-register.html')

class LoginView(View):
    def get(self,request):
        return render(request,'page-user-login.html')






# def register(sorov):
#     if sorov.method == 'POST' and sorov.POST.get('p') == sorov.POST.get('p2'):
#         u = User.objects.create_user(
#             username = sorov.POST.get('l'),
#             password = sorov.POST.get('p')
#         )
#
#         return redirect('login')
#     return render(sorov,'register.html')

