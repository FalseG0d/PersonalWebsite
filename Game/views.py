from django.shortcuts import render
from .models import *
# Create your views here.
def games(request):
    games=Game.objects.all()

    context={
        'games':games,
    }

    return render(request,"games.html",context)