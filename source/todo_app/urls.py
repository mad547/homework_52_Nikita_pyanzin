from django.urls import path
from todo_app.models import task_list, task_add, task_delete


urlpatterns = [
    path('tasks/', task_add),
    path('tasks/add/', task_add),
    path('tasks/delete/', task_delete),
]