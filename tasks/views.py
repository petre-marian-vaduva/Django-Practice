from django.shortcuts import render

tasks = ['test1', 'test2', 'test3']
# Create your views here.
def index(request):
    return render(request, 'tasks/index.html', {
        'tasks': tasks
    })

def add(request):
    return render(request, 'tasks/add.html')