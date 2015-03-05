from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label='username', min_length=3, max_length=20)
    password = forms.CharField(label='password', min_length=6, widget=forms.PasswordInput())

class PunchForm(forms.Form):
