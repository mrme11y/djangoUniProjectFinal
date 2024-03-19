from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Ticket
from .forms import TicketForm, LoginForm, UpdateTicket
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def home(request):
    return render(request, 'index.html')


@login_required
def create_ticket(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.creator = request.user
            ticket.save()
            messages.success(request, 'Ticket created successfully')
            return redirect('tickets_list')
    else:
        form = TicketForm()
    return render(request, 'create_ticket.html', {'form': form})


@login_required
def tickets_list(request):
    tickets = Ticket.objects.all()
    return render(request, 'tickets_list.html', {'tickets': tickets})


@login_required
def ticket_detail(request, ticket_id):
    ticket = Ticket.objects.get(id=ticket_id)
    return render(request, 'ticket_detail.html', {'ticket': ticket})


# Login a user
def user_login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
                messages.success(request, 'Login successful')
                return redirect('tickets_list')
    context = {'form': form}
    return render(request, 'user_login.html', context)


# Logout a user
@login_required(login_url='user_login')
def user_logout(request):
    auth.logout(request)
    messages.success(request, 'Logout successful')
    return redirect('user_login')


# Update a ticket
@login_required(login_url='user_login')
def update_ticket(request, ticket_id):
    ticket = Ticket.objects.get(id=ticket_id)
    form = UpdateTicket(instance=ticket)
    if request.method == 'POST':
        form = UpdateTicket(request.POST, instance=ticket)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ticket updated successfully')
            return redirect('tickets_list')
    context = {'form': form}
    return render(request, 'update_ticket.html', context)


# Delete a ticket
@login_required(login_url='user_login')
def delete_ticket(request, ticket_id):
    ticket = Ticket.objects.get(id=ticket_id)
    ticket.delete()
    messages.success(request, 'Ticket deleted successfully')
    return redirect('tickets_list')

