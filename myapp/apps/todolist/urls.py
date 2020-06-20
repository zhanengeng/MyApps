from django.urls import path
from . import views # 本地文件夹导入views
from .views import * 

urlpatterns = [
    path("", views.index, name="index"),
    path("index/", views.index, name="index"),
    path("todoAdd/", views.TodoAdd.as_view(), name="todoadd"), # 类视图用
]
