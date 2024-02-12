from django.shortcuts import render, get_object_or_404, redirect

from .models import Task
from .forms import TaskForm, UpdateTaskStatusForm, TaskEditForm

def task_list(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'task_list.html', {'tasks': tasks})

def dashboard(request):
    pending_tasks = Task.objects.filter(user=request.user, status='todo').count()
    completed_tasks = Task.objects.filter(user=request.user, status='done').count()
    
    return render(request, 'dashboard.html', {'pending_tasks': pending_tasks, 'completed_tasks': completed_tasks})

def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    update_status_form = None

    if request.method == 'POST':
        if 'status' in request.POST:
            update_status_form = UpdateTaskStatusForm(request.POST, instance=task)
            if update_status_form.is_valid():
                update_status_form.save()
        elif 'delete_task' in request.POST:
            task.delete()
            return redirect('task_list')

    else:
        update_status_form = UpdateTaskStatusForm(instance=task)

    return render(request, 'task_detail.html', {'task': task, 'update_task_status_form': update_status_form, 'task_id': task.id})

def task_edit(request, pk):
    task = get_object_or_404(Task, pk=pk)

    if request.method == 'POST':
        form = TaskEditForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_detail', pk=task.id)  # Redirect to task detail
    else:
        form = TaskEditForm(instance=task)

    return render(request, 'task_edit.html', {'form': form})

def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'task_form.html', {'form': form})

def task_edit(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'task_form.html', {'form': form})

def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('task_list')
