from django import forms
from todolist.models import Task
from django.forms import ModelForm


class Form(ModelForm):
    title = forms.CharField(max_length=255)
    description = forms.CharField(widget=forms.TextInput)
    class Meta:
        model = Task
        fields = ['title','description']
    