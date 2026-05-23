from django.db import models

# Create your models here.
STATUS_CHOICES = [
    ('new', 'Новая'),
    ('in_progress', 'В процессе'),
    ('done', 'Сделано'),
]

class Task(models.Model):
    description = models.TextField(null=False, blank=False, verbose_name='Описание')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new', verbose_name='Статус')
    due_date = models.DateField(null=True, blank=True, verbose_name='Дата выпонения')

    def __str__(self):
        return self.description[:50]

    class Meta:
        db_table = 'task'
        verbose_name = 'задача'