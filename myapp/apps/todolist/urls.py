from django.urls import path
from .views import * 

urlpatterns = [
    path("", IndexView.as_view(), name="index"),  
    path("<int:page_id>/", IndexView.as_view(), name="index"),  

    path("todoAdd/", TodoAddView.as_view(), name="todoadd"), 
    path("todoDelete/<int:del_id>/", TodoDeleteView.as_view(), name="tododelete"),
    path("todoEdit/<int:edit_id>/", TodoEditView.as_view(), name="todoedit"),
    path("deletedTodo/",DeletedTodoView.as_view(), name="deletedtodo"),
    path("deleteForever/<int:del_id>/",DeleteForeverView.as_view(), name="deleteforever"),
    path("restore/<int:res_id>/",TodoRestoreView.as_view(), name="restore"),
]
