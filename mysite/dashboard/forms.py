from django import forms
from .models import Client, Software

class NameForm(forms.Form):
    clinet_name = forms.CharField(label='Client name', max_length=100)
    country = forms.CharField(max_length=100)
    city = forms.CharField(max_length=150)
    longitude = forms.DecimalField(max_digits=9, decimal_places=5, required=False)
    latitude = forms.DecimalField(max_digits=9, decimal_places=5, required=False)

class ProjectForm(forms.Form):
    project_name = forms.CharField(label="Project name", max_length=100)
    project_num = forms.IntegerField()
    desc = forms.CharField(widget=forms.Textarea)
    client = forms.ModelChoiceField(queryset=Client.objects.all())
    soft = forms.ModelChoiceField(queryset=Software.objects.all())

class SoftwareForm(forms.Form):
    name = forms.CharField(label='Software name')
    desc = forms.CharField(widget=forms.Textarea)