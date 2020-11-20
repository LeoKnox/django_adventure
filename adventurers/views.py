from django.shortcuts import render, HttpResponse

def index(request):
    return render(request, 'adventurers/index.html', {})

def player(request, character_id):
    return HttpResponse("Character you are playing")

def create(request):
    return HttpResponse("Add new character")