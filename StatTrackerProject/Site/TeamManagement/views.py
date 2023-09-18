from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import RegisterForm, LoginForm, OrganizationCreationForm, TeamCreationForm, PlayerAddForm, UploadFileForm
from .models import Organization, Team, Player
from .helperMethods import handle_input_file
from io import TextIOWrapper

# Create your views here.
def teamManage(request):
    if (request.user.is_authenticated):
        if (request.user.has_organization):
            orgs = Organization.objects.filter(owner = request.user)
            return render(request, 'teamManagement/orgSelect.html', context = {'orgs': orgs})
        else:
            return redirect('createOrg')
    else:
        return redirect('login')

def loginView(request):
    message = ''
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid:
            user = authenticate(email = request.POST.get('email'), password = request.POST.get('password1'))
            if user is not None:
                login(request, user)
                message1 = f'Hello {user.firstName}! You have been logged in.'
                request.session['messages'] = [message1]
                return redirect('home')
            else:
                message = 'Login Failed.'
    else:
        form = LoginForm()
    return render(request, 'teamManagement/login.html', context = {'form': form, 'message': message})

def logoutView(request):
    logout(request)
    return redirect('home')

def registerView(request):
    message = ''
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            user = authenticate(email = form.cleaned_data.get('email'), password = form.cleaned_data.get('password1'))
            if user is not None:
                login(request, user)
                message1 = f'Welcome {user.firstName}! You have successfully registered.'
                request.session['messages'] = [message1]
                return redirect('home')
        else:
            print(form.errors)
    else:
        form = RegisterForm(request.POST)
    return render(request, 'teamManagement/register.html', context = {'form': form, 'message': message})
            

def userProfile(request):
    if request.user.is_authenticated:
        user = request.user
        return render(request, 'teamManagement/userProfile.html', context = {'messages': request.session['messages'], 'user': user})

def orgProfile(request, pk=None):
    if (request.user.is_authenticated):
        if (pk):
            org = Organization.objects.filter(pk=pk, owner = request.user)
            request.session['orgPk'] = pk
            return render(request, 'teamManagement/orgProfile.html', context = {'org': org, 'pk': pk})
        else:
            return redirect('teamManage')
    else:
        return redirect('login')

def teamList(request, pk=None):
    if (pk):
        org = Organization.objects.get(pk=pk, owner = request.user)
        teams = Team.objects.filter(org = org)
        return render(request, 'teamManagement/teamList.html', context = {'teams': teams, 'pk': pk})

    else:
        return redirect('teamManage')

def editTeam(request, pk=None, team_name=None):
    if (request.user.is_authenticated):
        if (pk and team_name):
            org = Organization.objects.get(pk=pk, owner = request.user)
            team = Team.objects.get(team_name = team_name, org = org)
            players = Player.objects.filter(team = team)
            if (request.method == 'POST'):
                individualForm = PlayerAddForm(request.POST)
                fileForm = UploadFileForm(request.POST, request.FILES)
                if individualForm.is_valid and request.POST.get('number') != None:
                    player = Player.create(
                        first_name = request.POST.get('first_name'), 
                        last_name = request.POST.get('last_name'),
                        number = request.POST.get('number'),
                        team = team
                    )
                    if len(Player.objects.filter(number = player.number)) == 0:
                        player.save()
                else:
                    print(individualForm.errors)

                if fileForm.is_valid and 'docfile' in request.FILES:
                    f = TextIOWrapper(request.FILES['docfile'].file, encoding=request.encoding)
                    handle_input_file(f, org, team)
            else:
                individualForm = PlayerAddForm(request.POST)
                fileForm = UploadFileForm()
            return render(request, 'teamManagement/editTeam.html', context = {'org': org, 'team': team, 'players': players, 'individualForm': individualForm, 'fileForm': fileForm})
        else:
            return redirect('teamManage')
    else:
        return redirect('login')

def addTeam(request, pk=None):
    if (request.user.is_authenticated):
        if (pk):
            if (request.method == 'POST'):
                form = TeamCreationForm(request.POST)
                if (form.is_valid):
                    org = Organization.objects.get(pk=pk, owner = request.user)
                    team = Team.create(
                        team_name = request.POST.get('team_name'),
                        org = org,
                    )
                    team.save()
                    return redirect('teamManage')
                else:
                    print(form.errors)
            else:
                form = TeamCreationForm(request.POST)
                return render(request, 'teamManagement/addTeam.html', context = {'form': form, 'pk': pk})
        else:
            return redirect('teamManage')
    else:
        return redirect('login')

def createOrg(request):
    if (request.user.is_authenticated):
        if (request.method == 'POST'):
            form = OrganizationCreationForm(request.POST)
            if (form.is_valid):
                org = Organization.create(
                    school_name = request.POST.get('school_name'),
                    org_type = request.POST.get('org_type'),
                    city = request.POST.get('city'),
                    state = request.POST.get('state'),
                    owner = request.user
                )

                org.save()
                request.user.has_organization = True
                request.user.save()
                return redirect('teamManage')
            else:
                print(form.errors)
        else:
            form = OrganizationCreationForm(request.POST)
        return render(request, 'teamManagement/createOrg.html', context = {'form': form, 'org_types': Organization.org_type_choices, 'states': Organization.state_choices})
    else:
        return redirect('login')