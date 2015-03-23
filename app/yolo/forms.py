from django import forms
from django.contrib.auth.models import User

class ChallengeForm(forms.Form):
    name = forms.CharField(label='Punch name', min_length=3, max_length=100)
    recipient = forms.CharField(label='Recipient')
    desc = forms.CharField(label='Description', min_length=3, max_length=500,
                                            widget=forms.Textarea)


class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password', 'first_name', 'last_name')

