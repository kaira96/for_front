from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from core.yasg import urlpatterns as docs_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('mainapp.urls')),
    path('api/', include('daily_diary.urls')),
    path('api/stocks/', include('stocks.urls')),
    path('api/', include('calendar_1.urls')),
    path('api/', include('staff.urls')),
    path('api/', include('sales_.urls')),
    path('api/', include('users.urls')),
    path('api/auth/', include('dj_rest_auth.urls')),
    path('api/auth/registration/', include('dj_rest_auth.registration.urls'))
]

urlpatterns += docs_urls
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
