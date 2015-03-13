from django import forms

class ChallangeForm(forms.Form):
    name = forms.CharField(label='Punch name', min_length=3, max_length=100)
    recipient = forms.CharField(label='Recipient')
    desc = forms.CharField(label='Description', min_length=3, max_length=500,
                                            widget=forms.Textarea)
