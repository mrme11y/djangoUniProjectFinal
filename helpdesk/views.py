from django.shortcuts import render, redirect


def home(request):
    return render(request, 'helpdesk/index.html')