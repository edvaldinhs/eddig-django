from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from .models import Player
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth import logout
import json

def index(request):
    return render(request, 'index.html')

def game(request):
    if request.user.is_authenticated:
        return render(request, 'game.html')
  
    return redirect('login')

def about(request):
    return render(request, 'about.html')

def ranking(request):
    players = Player.objects.all().order_by("flips", "time")
    return render(request, "ranking.html", {"players": players})

def basicRank(request): 
    players = Player.objects.all().order_by("flips", "time")
    return render(request, "basicRank.html", {"players": players})

def get(request):
    if request.method == 'GET':
        players = Player.objects.all().order_by("flips", "time").values()
        return JsonResponse(list(players), safe=False)
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)

def custom_logout(request):
    logout(request)
    return redirect('login') 

class CustomLoginView(LoginView):
    template_name = 'login.html'
    success_url = reverse_lazy('game') 
    
    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.filter(username=username).first()
        if not user:

            user = User.objects.create_user(username=username, password=password)
            messages.success(request, 'Usuário criado com sucesso! Faça login para continuar.')


        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(self.success_url)
        else:
            messages.error(request, 'Falha no login. Verifique as informações e tente novamente.')
            return render(request, self.template_name)

@csrf_exempt
def add(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)

            player = Player(
                name=data['name'],
                flips=data['flips'],
                time=data['time'],
                user=request.user
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