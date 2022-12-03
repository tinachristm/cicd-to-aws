from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("<span>Helllllo,</span>" + request.GET["name"])
