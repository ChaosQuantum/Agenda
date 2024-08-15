from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contact/', include('contact.urls')),
    path('to_do/', include('to_do.urls')),
    path('', views.index, name='index'),
]
