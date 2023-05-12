from django.shortcuts import render

from django.http import HttpResponse
from .models import Ticket
from .models import DrawResult

def create_ticket(request):
    if request.method == 'POST':
        representative_name = request.POST.get('representative_name')
        representative_email = request.POST.get('representative_email')
        ticket_number = request.POST.get('ticket_number')

        ticket = Ticket(
            representative_name=representative_name,
            representative_email=representative_email,
            ticket_number=ticket_number
        )
        ticket.save()

        return HttpResponse('Ticket purchased successfully!')
    else:
        return render(request, 'create_ticket.html')



def draw_results(request):
    latest_results = DrawResult.objects.latest('draw_date')
    results = latest_results.winning_numbers
    return render(request, 'draw_results.html', {'results': results})
