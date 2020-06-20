from django.urls import path
from . import views # 本地文件夹导入views

urlpatterns = [
    path("", views.index, name="index"),
    path("index/", views.index, name="index")
]
