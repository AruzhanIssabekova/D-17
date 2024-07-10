from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm

def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bboard:list')
    else:
        form = TaskForm()
    return render(request, 'task_form.html', {'form': form})

def list_tasks(request):
    tasks = Task.objects.all()
    return render(request, 'task_list.html', {'tasks': tasks})

def view_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    return render(request, 'task_detail.html', {'task': task})

def delete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    if request.method == 'POST':
        task.delete()
        return redirect('bboard:list')
    return render(request, 'task_confirm_delete.html', {'task': task})
