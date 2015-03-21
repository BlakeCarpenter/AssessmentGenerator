from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from assessmentgenerator.models import UserProfile

# Create your views here.

def dashboard(request):
    return render(request, 'assessmentgenerator/dashboard.html')
