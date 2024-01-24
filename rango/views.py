from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def index(request):
    about_page_link = "<a href='/rango/about/'>About</a>"
    return HttpResponse(
        f"Rango says hey there partner! Go to the {about_page_link} Page"
    )


def about(request):
    home_page_link = ": <a href='/rango/'>Index</a>."
    return HttpResponse(
        f"Rango says here is the about page. Back to the {home_page_link} Page"
    )
