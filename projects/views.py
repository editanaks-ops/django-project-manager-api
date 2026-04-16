from django.shortcuts import render, redirect
from .forms import ProjectForm
from .models import Project
from django.contrib.auth.decorators import login_required
from users.views import is_admin, is_manager
from .models import Task
from .forms import TaskForm
from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy

class ProjectListView(LoginRequiredMixin, ListView):
    model = Project
    template_name = 'projects/project_list.html'
    context_object_name = 'projects'
    login_url = 'login'


class ProjectCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Project
    form_class = ProjectForm
    template_name = 'projects/create_project.html'
    success_url = reverse_lazy('project_list')
    login_url = 'login'
    raise_exception = True

    def test_func(self):
        return hasattr(self.request.user, 'profile') and self.request.user.profile.role == 'admin'

@login_required
def project_list(request):
    projects = Project.objects.all()
    return render(request, 'projects/project_list.html', {'projects': projects})


@login_required
def create_project(request):
    if not is_admin(request.user):
        return redirect('project_list')

    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('project_list')
    else:
        form = ProjectForm()

    return render(request, 'projects/create_project.html', {'form': form})


@login_required
def update_project(request, pk):
    if not (is_admin(request.user) or is_manager(request.user)):
        return redirect('project_list')

    project = Project.objects.get(pk=pk)

    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('project_list')
    else:
        form = ProjectForm(instance=project)

    return render(request, 'projects/update_project.html', {'form': form, 'project': project})

@login_required
def delete_project(request, pk):
    if not is_admin(request.user):
        return redirect('project_list')

    project = Project.objects.get(pk=pk)
    project.delete()

    return redirect('project_list')
@login_required
def create_task(request):
    if not (is_admin(request.user) or is_manager(request.user)):
        return redirect('project_list')

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('project_list')
    else:
        form = TaskForm()

    return render(request, 'projects/create_task.html', {'form': form})

@login_required
def complete_task(request, pk):
    task = Task.objects.get(pk=pk)

    if request.user.profile.role == 'user' or request.user.profile.role == 'manager' or request.user.profile.role == 'admin':
        task.completed = True
        task.save()

    return redirect('project_list')

from rest_framework import generics
from .serializers import ProjectSerializer, TaskSerializer
from .permissions import IsAdminOrManagerOrReadOnly


class ProjectApiListCreateView(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAdminOrManagerOrReadOnly]


class TaskApiListCreateView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAdminOrManagerOrReadOnly]