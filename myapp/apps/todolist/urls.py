from django.urls import path
from .views import * 

urlpatterns = [
    path("", IndexView.as_view(), name="index"),  # 関数無し時用
    # path("index/", IndexView.as_view(), name="index"),
    path("<int:page_id>", IndexView.as_view(), name="index"),  # 関数有り時用
    path("todoAdd/", TodoAddView.as_view(), name="todoadd"), 
    path("todoDelete/<int:del_id>", TodoDeleteView.as_view(), name="tododelete"),
    path("todoEdit/<int:edit_id>", TodoEditView.as_view(), name="todoedit"),
]
