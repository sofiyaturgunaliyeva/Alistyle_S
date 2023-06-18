from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from asosiy.views import *
from userapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('asosiy/', include('asosiy.urls')),
    path('', HomeLoginsiz.as_view(), name = 'home-loginsiz'),
    path('userapp/',include('userapp.urls')),
    path('buyurtma/',include('buyurtma.urls')),
    path('logout/',LogoutView.as_view(), name = 'logout'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
