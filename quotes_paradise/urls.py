from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('landing.urls')),
    path('accounts/', include('accounts.urls')),
    path('quotes/', include('quotes.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
