from django.db import models

# Create your models here.
class Ticket(models.Model):
    representative_name = models.CharField(max_length=100)
    representative_email = models.EmailField()
    ticket_number = models.CharField(max_length=10)
    class Meta:
        app_label = 'tickets'
class DrawResult(models.Model):
    draw_date = models.DateField()
    winning_ticket_number = models.CharField(max_length=10)
    winning_numbers = models.CharField(max_length=20,default='0')
    class Meta:
        app_label = 'tickets'
