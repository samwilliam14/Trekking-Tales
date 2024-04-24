from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    
from django import forms
from .models import SlotReservation

class SlotReservationForm(forms.ModelForm):
    class Meta:
        model = SlotReservation
        fields = ['destination', 'duration', 'number_of_members', 'arrival_date', 'leaving_date', 'name', 'phone_number']
        widgets = {
            'arrival_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'leaving_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'destination': forms.TextInput(attrs={'class': 'form-control'}),
            # Add more widgets as needed
        }
        help_texts = {
            'destination': ('Enter the destination name.'),
            # Add more help texts as needed
        }

