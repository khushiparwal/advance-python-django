from django.shortcuts import render
from django.http import HttpResponse

def test_ors(request):
    return HttpResponse('<h1>Django project ors</h1>')
# Create your views here.
