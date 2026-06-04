from django.shortcuts import render, redirect, get_object_or_404
from todo_app.models import Task
from todo_app.forms import TaskForm


# Create your views here.
def task_list(request):
    tasks = Task.objects.all()
    context = {'tasks': tasks}
    return render(request, 'task_list.html', context)


def task_add(request):
    form = TaskForm()
    if request.method == 'GET':
        return render(request, 'task_add.html', {'form':form})
    elif request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
        return render(request, 'task_add.html', {'form':form})


def task_edit(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    form = TaskForm(instance=task)
    if request.method == 'GET':
        return render(request, 'task_edit.html', {'form':form, 'task':task})
    elif request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
        return render(request, 'task_edit.html', {'form':form, 'task':task})


def task_delete(request, task_id):
    task_id = request.GET.get('id')
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')


def task_detail(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    context = {'task': task}
    return render(request, 'task_detail.html', context)