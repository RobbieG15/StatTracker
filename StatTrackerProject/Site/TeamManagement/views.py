from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import RegisterForm, LoginForm

# Create your views here.
def home(request):
    return render(request, 'teamManagement/teamManage.html')

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
                return redirect('userProfile')
            else:
                message = 'Login Failed.'
    else:
        form = LoginForm()
    return render(request, 'teamManagement/login.html', context = {'form': form, 'message': message})

def logoutView(request):
    return

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
                return redirect('userProfile')
        else:
            
            print(form.errors)
    else:
        form = RegisterForm(request.POST)
    return render(request, 'teamManagement/register.html', context = {'form': form, 'message': message})
            

def userProfile(request):
    if request.user.is_authenticated:
        user = request.user
        return render(request, 'teamManagement/userProfile.html', context = {'messages': request.session['messages'], 'user': user})

def orgProfile(request):
    return

def teamList(request):
    return

def editTeam(request):
    return

def addTeam(request):
    return