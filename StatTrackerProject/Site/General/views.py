from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'General/home.html')

def pricing(request):
    return render(request, 'General/pricing.html')

def howToList(request):
    return render(request, 'General/howToList.html')

def FAQ(request):
    return render(request, 'General/FAQ.html')

def help(request):
    return render(request, 'General/help.html')

def about(request):
    return render(request, 'General/about.html')