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
    
    # ex: /dashboard/resources
    path('resources/', views.resources, name='dashboard-resources'),
    # ex: /dashboard/structures

    path('structures/', views.structures, name='dashboard-structures'),
    # ex: /dashboard/projects

    path('projects/', views.projects, name='dashboard-projects'),
    # ex: /dashboard/projects/101
    path('projects/<int:num>', views.project_detail, name='dashboard-project-detail'),

    # ex: /dashboard/projects/new
    path('projects/new/', views.NewProject.as_view(), name='dashboard-projects-new'),
    

    path('software/', views.softwares, name='dashboard-softwares'),
    path('software/new/', views.NewSoftware.as_view(), name='dashboard-softwares-new')
]