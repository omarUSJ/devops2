from rest_framework import serializers
from .models import Ticket, DrawResult

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'

class DrawResultSerializer(serializers.ModelSerializer):
    winning_ticket = serializers.CharField(source='winning_ticket_number')
    class Meta:
        model = DrawResult
        fields = '__all__'


