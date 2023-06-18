from django.urls import path
from .views import *
urlpatterns = [
    path('', HammaTanlanganlarView.as_view(), name = 'tanlanganlar'),
    path('shopping/', ShoppingView.as_view(), name = 'shopping'),
    path('profile/', ProfileView.as_view(), name = 'profile'),
    path('savat_k/<int:pk>/', MiqdorKamaytir.as_view()),
    path('savat_q/<int:pk>/', MiqdorQosh.as_view()),
    path('tanlangan_ochir/<int:pk>/', TanlanganOchirView.as_view()),
]