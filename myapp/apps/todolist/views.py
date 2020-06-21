from django.shortcuts import render, redirect
from .models import MyToDoList
from django.views import View 
from .forms import * 
from django.urls import reverse

# Create your views here.
class IndexView(View):
    def get(self, request):
        todolist = MyToDoList.objects.filter(is_deleted=False).order_by("-id") # 未論理削除のtodo内容のみ表示
        params = {'todolist':todolist}
        return render(request, 'todolist/index.html', params)

class TodoAddView(View):
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

class TodoDeleteView(View):
    # 削除フォームの表示画面
    def get(self, request, del_id):
        # 記入したtodo内容を取り出し
        tdl_obj = MyToDoList.objects.get(id=del_id)
        context = {
            "title":tdl_obj.title,
            "contents":tdl_obj.contents,
            "deadline":tdl_obj.deadline,
            "done":tdl_obj.done,
        }
        # todo内容をフォームに渡す
        form = ToDoDeleteForm(context)
        params = {
            "form":form,
            "del_id": del_id, 
        }
        return render(request, "todolist/todoDelete.html" , params)

    # 業務処理：論理削除
    def post(self, request, del_id):
        tdl_obj = MyToDoList.objects.get(id=del_id)
        tdl_obj.is_deleted = True
        tdl_obj.save()
        return redirect(reverse('todolist:index'))