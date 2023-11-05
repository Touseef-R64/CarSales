
from django.contrib import admin
from django.urls import path,include
from django.conf.urls import handler404, handler500
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('user.urls')),
    path('', include('cars.urls'))
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


# handler404 = custom_404_page