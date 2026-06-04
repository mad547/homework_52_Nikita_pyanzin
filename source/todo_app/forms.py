from django.core.exceptions import ValidationError
from django.forms import ModelForm, widgets
from todo_app.models import Task


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['description','status', 'due_date', 'details']
        widgets = {
            'description': widgets.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Описание задачи',
            }),
            'status': widgets.Select(attrs={
                'class': 'form-control',
            }),
            'due_date': widgets.DateInput(attrs={
                'class': 'form-control',
                'type': 'date',
            }),
            'details': widgets.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'placeholder': 'Подробное описание'
            }),
        }

    def clean(self):
        description = self.cleaned_data.get('description')
        details = self.cleaned_data.get('details')
        if description and details and description == details:
            raise ValidationError('Описание и подробное описание не могут совпадать')
        return super().clean()