# backend/urls.py

from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path("", include("pages.urls")),
    path('products/', include('products.urls')),  # Include the products app URLs
    path('chat/', include('chat.urls')),  # Include the chat app URLs
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)