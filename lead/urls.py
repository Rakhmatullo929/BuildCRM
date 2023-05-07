from django.urls import path
from . import views

urlpatterns = [
    path('add-lead/', views.add_lead, name='add_lead'),
    path('<int:pk>/', views.leads_detail, name='leads_detail'),
    path('<int:pk>/delete/', views.leads_delete, name='leads_delete'),
    path('<int:pk>/edit/', views.leads_edit, name='leads_edit'),
    path('lead_list/', views.lead_list, name='lead_list')
]