from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login
from django.forms import ValidationError
from django.utils.translation import ugettext as _

from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label='username', min_length=3, max_length=20)
    password = forms.CharField(label='password', min_length=6, widget=forms.PasswordInput())

def home(request):
    return render(request, 'yolopunch/index.html')

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
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
    return render(request, 'yolopunch/login.html', {'form' : form})

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
    return render(request, 'yolopunch/styleguide.html')
