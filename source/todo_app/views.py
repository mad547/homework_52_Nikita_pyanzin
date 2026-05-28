from django.shortcuts import render, redirect, get_object_or_404
from todo_app.models import Task, STATUS_CHOICES


# Create your views here.
def task_list(request):
    tasks = Task.objects.all()
    context = {'tasks': tasks}
    return render(request, 'task_list.html', context)


def task_add(request):
    if request.method == 'GET':
        context = {'status_choices': STATUS_CHOICES}
        return render(request, 'task_add.html', context)
    elif request.method == 'POST':
        description = request.POST.get('description', '').strip()
        status = request.POST.get('status', 'new')
        due_date = request.POST.get('due_date', '').strip() or None
        details = request.POST.get('details', '').strip()
        if description:
            Task.objects.create(
                description=description,
                status=status,
                due_date=due_date,
                details=details
            )
        return redirect('task_list')


def task_delete(request):
    task_id = request.GET.get('id')
    if task_id:
        try:
            task = Task.objects.get(id=int(task_id))
            task.delete()
        except Task.DoesNotExist:
            pass
    return redirect('task_list')


def task_detail(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    context = {'task': task}
    return render(request, 'task_detail.html', context)