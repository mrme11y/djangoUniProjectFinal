from django import forms
from .models import Ticket
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['first_name', 'last_name', 'email', 'phone', 'summary', 'description', 'assigned_to', 'status', 'helpdesk_agent_creator']


# Login a user
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())
