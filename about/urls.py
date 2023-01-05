from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('', views.about, name='about'),
    path('art_of_coding/', views.read_art_of_coding, name='read_art_of_coding'),
    path('clean_design/', views.read_clean_design, name='read_clean_design'),
    path('amazing_support/', views.read_amazing_support, name='read_amazing_support'),
    path('pages_about/', views.pages_about, name='pages_about'),
    path('about_people/', views.about_people, name='about_people')


]