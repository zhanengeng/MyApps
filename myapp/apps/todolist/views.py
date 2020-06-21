from django.shortcuts import render, redirect
from django.views import View
from django.urls import reverse
from django.core.paginator import Paginator
from .models import MyToDoList
from .forms import *

# Create your views here.
class IndexView(View):
    def get(self, request, page_id=1):
        todolist = MyToDoList.objects.filter(is_deleted=False).order_by("-id")  # 未論理削除のtodo内容のみ表示
        paginator = Paginator(todolist, 5)  # 全てのデータを5行づつページ分
        current_page = paginator.get_page(page_id)  # page_idのページを取得(画面に表示,default=1)
        nn_page_num = page_id + 2  # 2つあとのページ番号
        params = {
            "paginator":paginator,
            'current_page':current_page,
            "nn_page_num":nn_page_num,
            }
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
            "create_time":tdl_obj.create_time,
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

class TodoEditView(View):
    def get(self, request, edit_id):
        tdl_obj = MyToDoList.objects.get(id=edit_id)
        context = {
            "title":tdl_obj.title,
            "contents":tdl_obj.contents,
            "deadline":tdl_obj.deadline,
            "done":tdl_obj.done,
        }
        form = ToDoEditForm(context)
        params = {
            "form":form,
            "edit_id":edit_id,
        }
        return render(request, "todolist/todoEdit.html", params)

    def post(self, request, edit_id):
        tdl_obj = MyToDoList.objects.get(id=edit_id)
        tdl_obj.title = request.POST.get("title")
        tdl_obj.contents = request.POST.get("contents")
        tdl_obj.deadline = request.POST.get("deadline")
        if request.POST.get("done") == "on":
        # if "done" in request.POST:
            tdl_obj.done = True
        else:
            tdl_obj.done = False
        tdl_obj.save()
        return redirect(reverse('todolist:index'))
