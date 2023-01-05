from django.core.mail import EmailMultiAlternatives, send_mail
from django.shortcuts import render, redirect
from django.template.loader import get_template, render_to_string


from first_projet_django import settings


def index(request):
    return render(request, 'asentus/index.html')


def pricing(request):
    return render(request, 'asentus/pricing.html')


def contact(requests):
    return render(requests, 'asentus/contact.html')


def triangle_roof(requests):
    return render(requests, 'asentus/triangle_roof.html')


def curved_corners(requests):
    return render(requests, 'asentus/curved_corners.html')


def bird_on_green(requests):
    return render(requests, 'asentus/bird_on_green.html')

