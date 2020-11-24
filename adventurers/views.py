from django.shortcuts import render, HttpResponse

from .models import Adventurer

def index(request):
    adv_data = Adventurer.objects.values()
    return render(request, 'adventurers/index.html', {'adv_data': adv_data})

def player(request, character_id):
    adv = Adventurer.objects.filter(id=character_id).first()
    return render(request, 'adventurers/player.html', {'adv':adv})

def create(request):
    return render(request, 'adventurers/create.html')

def creater(request):
    return render(request, 'adventurers/index.html')