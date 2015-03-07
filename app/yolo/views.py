from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login
from django.forms import ValidationError
from django.utils.translation import ugettext as _

from yolo import forms


def home(request):
    challange_form = forms.ChallangeForm()
    return render(request, 'yolo/index.html', {'challange_form' : challange_form})

def login(request):
    if request.method == 'POST':
        login_form = forms.LoginForm(request.POST)
        if login_form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    #redirect
                else:
                    pass
                    #return render(request, 'yolopunch/login.html', {'form': form})
            else:
                login_form.add_error(None, ValidationError(
                    _('Invalid username or password'),
                    code='login_error',
                ))

    else:
        login_form = forms.LoginForm()
    return render(request, 'yolo/login.html', {'form' : login_form})

def logout(request):
    pass

def register(request):
    if request.user.is_authenticated():
        return redirect('/' + request.user.username + '/')

        if request.method == 'POST':
            register_form = forms.RegisterForm(request.POST)
            if register_form.is_valid():
                #email confirmation mechanism here
                pass
        else:
            register_form = forms.RegisterForm()
        return render(request, 'yolo/register.html', {'form' : register_form})

def following(request):
    pass

def followers(request):
    pass


def search(request):
    pass

def top(request):
    pass

def user(request):
    pass

def punches(request):
    pass


def styleguide(request):
    return render(request, 'yolo/styleguide.html')
