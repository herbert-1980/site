from django.contrib import admin
from django.urls import path, include # adicionar include
from django.conf import settings
from django.conf.urls.static import static 
from django.contrib.auth import urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')), # url do accounts
    path('accounts/', include('accounts.urls')), # url do accounts
    path('', include('pages.urls')), # url do app
    path('perfil/', include('perfil.urls')), # url do perfil
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) # Adicionar Isto
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # Adicionar Isto