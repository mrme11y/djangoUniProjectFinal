from django import forms
from .models import Ticket
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['summary', 'description']


# Login a user
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())
