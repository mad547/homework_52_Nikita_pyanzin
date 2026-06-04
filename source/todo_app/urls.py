from django.urls import path
from todo_app.views import task_list, task_add, task_edit, task_delete, task_detail


urlpatterns = [
    path('tasks/', task_list, name='task_list'),
    path('tasks/add/', task_add, name='task_add'),
    path('tasks/<int:task_id>/edit/', task_edit, name='task_edit'),
    path('tasks/<int:task_id/delete/', task_delete, name='task_delete'),
    path('tasks/<int:task_id>/', task_detail, name='task_detail'),
]