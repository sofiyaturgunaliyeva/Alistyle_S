from django.urls import path
from .views import *
urlpatterns = [
    path('', HammaTanlanganlarView.as_view(), name = 'tanlanganlar'),
    path('savatlar/', ShoppingView.as_view(), name = 'shopping'),
    path('buyurtmalar/', BuyurtmaView.as_view(), name = 'buyurtmalar'),
    path('savat_k/<int:pk>/', MiqdorKamaytir.as_view()),
    path('savat_q/<int:pk>/', MiqdorQosh.as_view()),
    path('tanlangan_ochir/<int:pk>/', TanlanganOchirView.as_view()),
    path('savatitem_ochir/<int:pk>/', SavatItemOchirView.as_view()),
    path('item_qosh/<int:pk>/', SavatItemQosh.as_view(), name='buyurtma_qosh'),
    path('tanlangan_qosh/<int:pk>/', TanlanganQosh.as_view()),
    path('buyurtma_qosh/<int:pk>/', BuyurtmaQosh.as_view()),
]