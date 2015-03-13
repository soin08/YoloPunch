from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login
from django.forms import ValidationError
from django.utils.translation import ugettext as _
from yolo.models import Challenge

from yolo import forms


def home(request):
    challange_form = forms.ChallangeForm()
    return render(request, 'yolo/index.html', {'challange_form' : challange_form})

def top_users(request):
    return render(request, 'yolo/top.html', {'action_name': 'users'})

def following(request, username):
    user = get_object_or_404(User, username=username)
    #get following list and pass in to the template
    return render(request, 'yolo/following_followers.html', {'user': user, 'action_name': 'following'})

def followers(request, username):
    user = get_object_or_404(User, username=username)
    #get followers list and pass in to the template
    return render(request, 'yolo/following_followers.html', {'user': user, 'action_name': 'followers'})


def search(request):
    return render(request, 'yolo/search.html')

def top_all(request):
    return render(request, 'yolo/top.html', {'action_name': 'all'})

def top_users(request):
    return render(request, 'yolo/top.html', {'action_name': 'users'})

def top_challenges(request):
    return render(request, 'yolo/top.html', {'action_name': 'punches'})

def user(request, username):
    user = get_object_or_404(User, username=username)
    return render(request, 'yolo/user.html', {'user': user})

def challanges_all(request, username):
    #show both created and completed challanges
    #challanges =
    user = get_object_or_404(User, username=username)
    return render(request, 'yolo/challenges.html', {'user': user, 'action_name':'all'})

def challanges_created(request, username):
    #show created challanges
    #challanges =
    user = get_object_or_404(User, username=username)
    return render(request, 'yolo/challenges.html', {'user': user, 'action_name':'created'})

def challanges_completed(request, username):
    #show created challanges
    #challanges =
    user = get_object_or_404(User, username=username)
    return render(request, 'yolo/challenges.html', {'user': user, 'action_name':'completed'})


def styleguide(request):
    return render(request, 'yolo/styleguide.html')
