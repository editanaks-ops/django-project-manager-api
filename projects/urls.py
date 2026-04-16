from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProjectListView.as_view(), name='project_list'),
    path('create/', views.ProjectCreateView.as_view(), name='create_project'),
    path('update/<int:pk>/', views.update_project, name='update_project'),
    path('delete/<int:pk>/', views.delete_project, name='delete_project'),
    path('task/create/', views.create_task, name='create_task'),
    path('task/complete/<int:pk>/', views.complete_task, name='complete_task'),
    path('api/projects/', views.ProjectApiListCreateView.as_view(), name='api_projects'),
    path('api/tasks/', views.TaskApiListCreateView.as_view(), name='api_tasks'),
]