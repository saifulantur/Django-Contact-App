from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# customizing admin texts
admin.site.site_header = 'Contacts'
admin.site.index_title = 'Welcome to our app'
admin.site.site_title = 'control panel'