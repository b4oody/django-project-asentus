from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('triangle_roof/', views.triangle_roof, name='triangle_roof'),
    path('curved_corners/', views.curved_corners, name='curved_corners'),
    path('bird_on_green/', views.bird_on_green, name='bird_on_green')

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)