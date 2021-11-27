from django.shortcuts import render
from django.http import HttpResponse


task = ['foo', 'bar', 'baz']

def index(request):
    return render(request, "todoapp/index.html", {
        'tasks' : task
    })
