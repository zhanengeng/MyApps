from django.urls import path
from .views import * 

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("index/", IndexView.as_view(), name="index"),
    path("todoAdd/", TodoAddView.as_view(), name="todoadd"), 
    path("todoDelete/<int:del_id>", TodoDeleteView.as_view(), name="tododelete"),
    path("todoEdit/<int:edit_id>", TodoEditView.as_view(), name="todoedit"),
]
