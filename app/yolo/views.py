from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login
from django.forms import ValidationError
from django.utils.translation import ugettext as _

from yolo import forms


def home(request):
    punch_form = forms.PunchForm()
    print(punch_form)
    return render(request, 'yolo/index.html', {'punch_form' : punch_form})

def login(request):
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
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
                form.add_error(None, ValidationError(
                    _('Invalid username or password'),
                    code='login_error',
                ))

    else:
        form = LoginForm()
    return render(request, 'yolo/login.html', {'form' : form})

def logout(request):
    pass

def registration(request):
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
