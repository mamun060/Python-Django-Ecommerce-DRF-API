from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path , include

urlpatterns = [
    # django silk package for profiling and url optimization
    path('silk/', include('silk.urls', namespace='silk')),
    # frontend route file include here
    path('', include('backend.urls')),
    # api route file include here
    path('v1/api/', include('backend.apiUrls')),
    # Django super admin url
    path('admin/', admin.site.urls),
]

# media file access
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)