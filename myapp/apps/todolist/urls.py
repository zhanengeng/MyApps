from django.urls import path
from .views import * 

urlpatterns = [
    path("", Index.as_view(), name="index"),
    path("index/", Index.as_view(), name="index"),
    path("todoAdd/", TodoAdd.as_view(), name="todoadd"), 
    path("todoDelete/<int:del_id>", TodoDelete.as_view(), name="tododelete")
]
