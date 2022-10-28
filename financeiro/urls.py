from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from funcinarios.views import index
admin.site.site_title = 'XFLAVORS'
admin.site.site_header = 'XFLAVORS ADMIN'
admin.site.index_title = 'XFLAVORS ADMIN'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='home'),


]   + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)