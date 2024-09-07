from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from .models import Player
import json

def index(request):
    return render(request, 'index.html')

def game(request):
    return render(request, 'game.html')

def about(request):
    return render(request, 'about.html')

def ranking(request):
    players = Player.objects.all().order_by("flips", "-time")
    return render(request, "ranking.html", {"players": players})

def basicRank(request): 
    players = Player.objects.all().order_by("flips", "-time")
    return render(request, "basicRank.html", {"players": players})

def get(request):
    if request.method == 'GET':
        players = Player.objects.all().order_by("flips", "-time").values()
        return JsonResponse(list(players), safe=False)
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)

@csrf_exempt
def add(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)

            player = Player(
                name=data['name'],
                flips=data['flips'],
                time=data['time'],
            )
            player.save()
            return JsonResponse({'status': 'success'}, status=201)
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)

def delete(request, id):
    player=Player.objects.get(id=id)
    player.delete()
    return redirect("/")