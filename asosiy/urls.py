
from django.urls import path
from .views import *

urlpatterns = [
    path('', Home.as_view(), name = 'home'),
    path('<int:pk>/mahsulotlar/', MahsulotlarView.as_view(), name = 'mahsulotlar'),
    path('bolimlar/', BolimlarView.as_view(), name = 'bolimlar'),
    path('mahsulot/<int:pk>/', BittaMahsulotView.as_view(), name = 'mahsulot'),
]
