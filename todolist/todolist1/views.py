from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import MyToDoList 
#ここで.が必須！なぜならそれがないと他のpythonファイルはrunできない。このファイルならrunできるのみ
from .forms import todoAddForm

def index(request):
    all_todo = MyToDoList.objects.all()
    params = {
        'todolist': all_todo,
    }

    return render(request, 'todolist1/index.html', params)
    # 第３引数追加

def todoAdd(request):
    form = todoAddForm
    params = {
        'form':form
    }
    if(request.method == 'POST'):
        mtdl = MyToDoList()
        mtdl.title = request.POST('title')
        mtdl.contents = request.POST['contents']
        mtdl.deadline = request.POST['deadline']
        mtdl.save()
        return redirect(to="/todolist")

    return render(request,'todolist1/todoAdd.html', params)


