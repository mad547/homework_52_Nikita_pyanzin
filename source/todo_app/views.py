from django.http import HttpResponseRedirect
from django.shortcuts import render
from todo_app.models import Task, STATUS_CHOICES


# Create your views here.
def task_list(request):
    tasks = Task.objects.all()
    context = {'tasks': tasks}
    return render(request, 'task_list.html', context)


def task_add(request):
    if request.method == 'GET':
        context = {'status_choises': STATUS_CHOICES}
    elif request.method == 'POST':
        description = request.POST.get('description', '').strip()
        status = request.POST.get('status', 'new')
        due_date = request.POST.get('due_date', '').strip() or None
        if description:
            Task.objects.create(
                description=description,
                status=status,
                due_date=due_date,
            )
        return HttpResponseRedirect('/tasks/')

def task_delete(request):
    task_id = request.GET.get('id')
    if task_id:
        try:
            task = Task.objects.get(id=int(task_id))
            task.delete()
        except Task.DoesNotExist:
            pass
    return HttpResponseRedirect('/tasks/')