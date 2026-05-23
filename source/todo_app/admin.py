from django.contrib import admin
from todo_app.models import Task

# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'description', 'status', 'due_date']
    list_filter = ['status']
    search_fields = ['description']

admin.site.register(Task, TaskAdmin)