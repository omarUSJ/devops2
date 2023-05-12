from rest_framework import generics
from .models import Ticket, DrawResult
from .serializers import TicketSerializer, DrawResultSerializer

class TicketListCreateAPIView(generics.ListCreateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

class DrawResultListCreateAPIView(generics.ListCreateAPIView):
    queryset = DrawResult.objects.all()
    serializer_class = DrawResultSerializer

