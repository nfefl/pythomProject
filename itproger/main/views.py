from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    data = {
        'tittle': 'Rhythme Riddle'
    }
    return render(request, 'home.html', data)

def twitch(request):
    return render(request, 'twitch.html')
def playlists(request):
    return render(request, 'playlists.html')
def sub(request):
    return render(request, 'sub.html')
def puzzle(request):
    return render(request, 'puzzle.html')

def music(request):
    return render(request, 'music.html')

def acc(request):
    return render(request, 'acc.html')

def card(request):
    return render(request, 'card.html')
