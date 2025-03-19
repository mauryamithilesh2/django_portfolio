from django import forms
from .models import Clients

class ClientForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Email'}))
    contact = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Contact'}))

    class Meta:
        model = Clients
        fields = ['name', 'email', 'contact']


    