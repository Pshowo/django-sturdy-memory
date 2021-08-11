from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    # ex: /dashboard/clients
    path('clients/', views.clients, name='dashboard-clients'),
    # ex: /dashboard/clients/101
    path('clients/<int:num>', views.client_detail, name='dashboard-client_detail'),
    # ex: /dashboard/clients/new_client
    path('clients/new_client/', views.NewClient.as_view(), name='dashboard-new_client'),
    # ex: /dashboard/errors
    path('errorslog/', views.errorslog, name='dashboard-errorslog'),
    # ex: /dashboard/structures
    path('structures/', views.structures, name='dashboard-structures'),
    # ex: /dashboard/projects
    path('projects/', views.projects, name='dashboard-projects'),
]