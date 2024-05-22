from django.shortcuts import render, get_object_or_404, redirect
from .models import Project, Task
from .forms import ProjectForm, TaskForm
from django.contrib.auth.decorators import login_required

from rest_framework import viewsets, permissions
from .models import ChatMessage
from .serializers import ChatMessageSerializer

@login_required
def project_list(request):
    projects = Project.objects.all()
    return render(request, 'tasks/project_list.html', {'projects': projects})

@login_required
def project_detail(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    tasks = project.task_set.all()
    return render(request, 'tasks/project_detail.html', {'project': project, 'tasks': tasks})

@login_required
def task_detail(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    return render(request, 'tasks/task_detail.html', {'task': task, 'project_id':1})

@login_required
def add_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('project_list')
    else:
        form = ProjectForm()
    return render(request, 'tasks/project_form.html', {'form': form})

@login_required
def add_task(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.project = project
            task.save()
            return redirect('project_detail', project_id=project.id)
    else:
        form = TaskForm()
    return render(request, 'tasks/task_form.html', {'form': form, 'project': project})


@login_required
def delete_task(request, task_id):
    if request.method == 'GET': #needs to convert it into DELETE future implementation
            obj_instance = Task.objects.get(id=task_id)
            print("----------------------")
            print(obj_instance.delete())
            print("task deleted successfully")
            projects = Project.objects.all()
            return render(request, 'tasks/project_list.html', {'projects': projects})
    else:
        print("task not deleted")
        projects = Project.objects.all()
        return render(request, 'tasks/project_list.html', {'projects': projects})

@login_required
def chatroom(request, task_id):
    return render(request, 'chatroom.html', {
        'task_id': task_id,
        'username': request.user.username
    })

    
class ChatMessageViewSet(viewsets.ModelViewSet):
    queryset = ChatMessage.objects.all()
    serializer_class = ChatMessageSerializer
    permission_classes = [permissions.IsAuthenticated]