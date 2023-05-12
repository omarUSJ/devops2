from django.urls import path
from . import views,views_api

urlpatterns = [
    path('create_ticket/', views.create_ticket, name='create_ticket'),
    path('draw_results/', views.draw_results, name='draw_results'),
 # API views
    path('api/tickets/', views_api.TicketListCreateAPIView.as_view(), name='ticket_list_create_api'),
    path('api/draw_results/', views_api.DrawResultListCreateAPIView.as_view(), name='draw_result_list_create_api'),

]

