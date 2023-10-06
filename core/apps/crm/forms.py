from django import forms
from ckeditor.widgets import CKEditorWidget
from .models import Project, Task
from django.contrib.auth.models import User  # Django's built-in User model


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'start_date', 'end_date']
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        )
    )
    description = forms.CharField(widget=CKEditorWidget())
    start_date = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'class': 'form-control',
                'id': 'datepicker-icon-prepend-start',
                'value': '2020-06-20',
                # Add other attributes as needed
            }
        )
    )

    end_date = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'class': 'form-control',
                'id': 'datepicker-icon-prepend-end',
                'value': '2020-06-20',
            }
        )
    )

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'assigned_to', 'completed']

    title = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        max_length=200,
    )

    description = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control'}),
        required=False,
    )

    due_date = forms.DateField(
        widget=forms.DateInput(attrs={'class': 'form-control datepicker'}),
    )

    assigned_to = forms.ModelChoiceField(
        queryset=User.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        required=False,
    )

    completed = forms.BooleanField(
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        required=False,
    )

