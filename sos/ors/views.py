from django.shortcuts import render
from django.http import HttpResponse

def test_ors(request):
    return HttpResponse('<h1>Django project ors</h1>')
# Create your views here.
def welcome(request):
    return render(request, "welcome.html")

def signup(request):
    print(request.GET.get("Firstname"))
    print(request.GET.get("Lastname"))
    print(request.GET.get("Email"))
    print(request.GET.get("DOB"))
    print(request.GET.get("Address"))
    return render(request, "registration.html")