from django.shortcuts import render
# from django.http import HttpResponse
from .models import MyToDoList
# Create your views here.
def index(request):
    todolist = MyToDoList.objects.filter(is_deleted=False) # 未削除の任務のみ表示
    # todolist = MyToDoList.objects.all()
    params = {'todolist':todolist}
    return render(request, 'todolist/index.html', params)