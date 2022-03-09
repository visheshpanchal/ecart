from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include("home.urls")),
    path("account/",include("accounts.urls")),
    path('category/',include('product.urls')),
   
    
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)

