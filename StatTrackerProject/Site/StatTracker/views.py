from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.apps import apps
from .forms import GameCreationForm

# Model imports
Organization = apps.get_model('TeamManagement', 'Organization')
Team = apps.get_model('TeamManagement', 'Team')
Player = apps.get_model('TeamManagement', 'Player')
Game = apps.get_model('TeamManagement', 'Game')
FootballStat = apps.get_model('TeamManagement', 'FootballStat')

# Create your views here.
def home(request):
    return render(request, 'statTracker/statTracker.html')

def addGames(request, pk):
    if (request.user.is_authenticated):
        if (pk):
            org = Organization.objects.get(pk=pk, owner = request.user)
            teams = Team.objects.filter(org = org)
            if (request.method == 'POST'):
                gameCreationForm = GameCreationForm(request.POST)
                if gameCreationForm.is_valid:
                    game = Game.create(
                        org = org,
                        homeTeam = Team.objects.get(team_name = request.POST.get('homeTeam')), 
                        awayTeam = Team.objects.get(team_name = request.POST.get('awayTeam')),
                        dateTime = request.POST.get('dateTime')
                    )
                    game.save()
                    return redirect('addGames', pk)
                else:
                    print(gameCreationForm.errors)
            else:
                gameCreationForm = GameCreationForm(request.POST)
            games = Game.objects.filter(org = org)
            return render(request, 'statTracker/addGames.html', context = {'org': org, 'teams': teams, 'games': games, 'gameCreationForm': gameCreationForm, 'pk': pk})
        else:
            return redirect('home')
    else:
        return redirect('login')

def startGame(request, pk = None):
    if request.user.is_authenticated:
        if pk != None:
            if 'orgPk' in request.session:
                org = Organization.objects.get(pk=request.session['orgPk'])
                game = Game.objects.get(org=org, pk=pk)
                return render(request, 'statTracker/startGame.html', context={'game': game})
            else:
                return redirect('teamManage')
        else:
            return redirect('teamManage')
    else:
        return redirect('login')

def gameList(request, pk):
    if request.user.is_authenticated:
        org = Organization.objects.get(pk=pk)
        games = Game.objects.filter(org=org)
        return render(request, 'statTracker/gameList.html', context={'org': org, 'games': games, 'pk': pk})
    else:
        return redirect('login')

def trackGame(request, pk):
    pass

def editGame(request, pk):
    pass