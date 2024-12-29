from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include(('users.urls', 'users'), namespace='users')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
]
