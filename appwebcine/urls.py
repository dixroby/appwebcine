from django.contrib import admin
from django.urls import path , include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path ('',include('core.urls')),
    path ('accounts/',include('django.contrib.auth.urls')),
    
]

admin.site.site_header = "Administracion de Cine Perú"
admin.site.index_title = "Modulos de administración"
admin.site.site_title = "Cine Perú"

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)