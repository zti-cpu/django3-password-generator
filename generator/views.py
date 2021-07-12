from django.shortcuts import render
from django.http import HttpResponse
import random


# Create your views here.

def home(request):
    return render(request, 'generator/home.html')
def help(request):
    return render(request, 'generator/help.html')


def password(request):
    characters = list("qwertyuiopasdfghjklzxcvbnm")
    lenght = int(request.GET.get("lenght"))
    thepassword = ""
    if request.GET.get("uppercase"):
        characters.extend(list("qwertyuiopasdfghjklzxcvbnm".upper()))
    if request.GET.get("special"):
        characters.extend(list("%*)?@#$~".upper()))
    if request.GET.get("numbers"):
        characters.extend(list("1234567890".upper()))
    for x in range(lenght):
        thepassword+=random.choice(characters)
    return render(request, 'generator/password.html', {"password": thepassword})
