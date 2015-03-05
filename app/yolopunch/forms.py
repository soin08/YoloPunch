from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label='username', min_length=3, max_length=20)
    password = forms.CharField(label='password', min_length=6,
                                                    widget=forms.PasswordInput())

class PunchForm(forms.Form):
    name = forms.CharField(label='Punch name', min_length=3, max_length=100)
    recipient = forms.CharField(label='Recipient')
    desc = forms.CharField(label='Description', min_length=3, max_length=500,
                                            widget=forms.Textarea)
