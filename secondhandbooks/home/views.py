from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Books


def index(request):
    template_html = 'home/home.html'

    books = Books.objects.all()

    return render(request, template_html, {'books':books})