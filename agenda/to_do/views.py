from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm
from django.contrib import messages

def index(request):
    todos=Todo.objects.filter(title__contains=request.GET.get('search', ''))
    context={
        'todos':todos
    }
    return render(request, 'to_do/index.html', context)

def view(request, id):
    todo=Todo.objects.get(id=id)
    context={
        'todo':todo
    }
    return render(request, 'to_do/detail.html', context)

def edit(request, id):
    todo=Todo.objects.get(id=id)

    if request.method=='GET':
        form=TodoForm(instance=todo)
        context={
            'form':form,
            'id':id,
        }
        return render(request, 'to_do/edit.html', context)
    
    if request.method=='POST':
        form=TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
        messages.success(request, 'Tarea actualizada')
        context={
            'form':form,
            'id':id
        }
        return render(request, 'to_do/edit.html', context)
                  

def create(request):
    if request.method=='GET':
        form=TodoForm()
        context={
            'form':form
        }
        return render(request, 'to_do/create.html', context)
    if request.method=='POST':
        form=TodoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('to_do')

    
def delete (request, id):
    todo=Todo.objects.get(id=id)
    todo.delete()
    return redirect('to_do')
