from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include(('users.urls', 'users'), namespace='users')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('music/', include(('music.urls', 'music'), namespace='music')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
