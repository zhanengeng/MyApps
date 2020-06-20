from django.shortcuts import render, redirect
from .models import MyToDoList
from django.views import View 
from .forms import * 
from django.urls import reverse

# Create your views here.
class Index(View):
    def get(self, request):
        todolist = MyToDoList.objects.filter(is_deleted=False).order_by("-id") # 未削除の任務のみ表示
        params = {'todolist':todolist}
        return render(request, 'todolist/index.html', params)

class TodoAdd(View):
    def get(self, request):
        form = ToDoAddForm()
        params={
            "form":form,
        }
        return render(request, 'todolist/todoAdd.html', params)
    def post(self, request):
        title = request.POST.get("title")
        contents = request.POST.get("contents")
        deadline = request.POST.get("deadline")
        MyToDoList.objects.create(title=title, contents=contents, deadline=deadline)
        return redirect(reverse('todolist:index'))

