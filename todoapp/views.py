from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django import forms
from django.urls import reverse


task = ['foo', 'bar', 'baz']

class NewTextForm(forms.Form):
    tasks = forms.CharField(label="New Task:")

def index(request):
    return render(request, "todoapp/index.html", {
        'tasks' : task,
        'form' : NewTextForm(),
    })
