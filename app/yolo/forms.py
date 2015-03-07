from django import forms

from yolo import validators as v

class LoginForm(forms.Form):
    username = forms.CharField(label='username', min_length=3, max_length=20,
                                                    validators=[v.UsernameValidator()])
    password = forms.CharField(label='password', min_length=6,
                                                    widget=forms.PasswordInput())

class RegisterForm(forms.Form):
    first_name = forms.CharField(label='First name', min_length=1, max_length=50)
    last_name = forms.CharField(label='Last name', min_length=1, max_length=50)
    username = forms.CharField(label='username', min_length=3, max_length=20,
                                                    validators=[v.UsernameValidator()])

class ChallangeForm(forms.Form):
    name = forms.CharField(label='Punch name', min_length=3, max_length=100)
    recipient = forms.CharField(label='Recipient')
    desc = forms.CharField(label='Description', min_length=3, max_length=500,
                                            widget=forms.Textarea)
