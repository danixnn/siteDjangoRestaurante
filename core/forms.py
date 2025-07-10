from django import forms

class SubForm(forms.Form):
    email = forms.EmailField(label='Email', max_length=100)
