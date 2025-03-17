from django import forms
from .models import Clients

# class ClientForm(forms.Form):
#     name=forms.CharField()
#     email=forms.EmailField()
#     contact=forms.IntegerField()

class ClientForm(forms.ModelForm):
    class Meta:
        model = Clients
        fields = ['name', 'email', 'contact']