from django import forms
from django.forms import ModelForm

from .models import *


class TaskForm(forms.ModelForm):
	title= forms.CharField()

	class Meta:
		model = Task
		fields = '__all__'
