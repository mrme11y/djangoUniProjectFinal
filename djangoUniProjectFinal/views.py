from django.shortcuts import render, redirect
from django.http import HttpResponse
# from .forms import CreateUserForm, LoginForm, CreateRecordForm, UpdateRecordForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# from .models import Record
from django.contrib.staticfiles.storage import staticfiles_storage


def home(request):
    return render(request, 'index.html')
