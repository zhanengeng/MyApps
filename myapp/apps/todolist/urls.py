from django.urls import path
# from . import views
from .views import * 

urlpatterns = [
    path("", Index.as_view(), name="index"),
    path("index/", Index.as_view(), name="index"),
    path("todoAdd/", TodoAdd.as_view(), name="todoadd"), 
]
