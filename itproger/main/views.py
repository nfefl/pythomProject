from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')
def about(request):
    return render(request, 'about.html')

def contacts(request):
    return render(request, 'contacts.html')

def tg(request):
    return render(request, 'tg.html')

def twitch(request):
    return render(request, 'twitch.html')