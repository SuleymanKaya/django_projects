from .forms import ListForm
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Todos

def index(request):
    if request.method=="POST":
        form = ListForm(request.POST or None)
        if form.is_valid:
            form.save()
            todo_lists = Todos.objects.all()
            return render(request, "todo_app/index.html", {"todo_list": todo_lists})
    else:             
        todo_lists = Todos.objects.all()
        return render(request, "todo_app/index.html", {"todo_list": todo_lists})
        #return HttpResponse("This is Index Page")

def about(request):
    return render(request, "todo_app/about.html")
    #return HttpResponse("This is About Page")

def create(request):
    if request.method=="POST":
        form = ListForm(request.POST or None)
        if form.is_valid:
            form.save()
            todo_lists = Todos.objects.all()
            return render(request, "todo_app/index.html", {"todo_list": todo_lists})
    else:     
        return render(request, "todo_app/create.html")

def delete(request, Todos_id):
    todo = Todos.objects.get(pk=Todos_id)
    todo.delete()
    return redirect("index")

def yes_finished(request, Todos_id):
    todo = Todos.objects.get(pk=Todos_id)
    todo.finished = False
    todo.save()
    return redirect("index")

def no_finished(request, Todos_id):
    todo = Todos.objects.get(pk=Todos_id)
    todo.finished = True
    todo.save()
    return redirect("index")

def update(request, Todos_id):
    if request.method=="POST":
        todo_list = Todos.objects.get(pk=Todos_id)
        form = ListForm(request.POST or None, instance=todo_list)
        if form.is_valid:
            form.save()
            return redirect("index")
    else:   
        return render(request, "todo_app/update.html")