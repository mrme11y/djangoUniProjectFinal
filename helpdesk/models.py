from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User


class Ticket(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=20)
    summary = models.CharField(max_length=100)
    description = models.TextField()
    helpdesk_agent_creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_tickets')
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='assigned_tickets', null=True, blank=True)
    status = models.CharField(max_length=20, choices=[('New', 'New'), ('In Progress', 'In Progress'), ('Closed', 'Closed')], default='New')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.summary
