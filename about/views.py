from django.http import HttpResponse
from django.shortcuts import render


def about(request):
    return render(request, 'asentus/about.html')



def read_art_of_coding(request):
    return render(request, 'about/art_of_coding.html')

def read_clean_design(request):
    return render(request, 'about/clean_design.html')

def read_amazing_support(request):
    return render(request, 'about/amazing_support.html')

def pages_about(request):
    return render(request, 'about/pages_about.html')

def about_people(request):
    return render(request, 'about/about_people.html')