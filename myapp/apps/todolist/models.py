from django.db import models
from db.base_model import BaseModel

# Create your models here.
class MyToDoList(BaseModel):
    title = models.CharField(max_length=255, verbose_name="タイトル")
    contents = models.TextField(verbose_name="詳細")
    deadline = models.DateField(verbose_name="締切")
    done = models.BooleanField(default=False, verbose_name="完成")

    def __str__(self):
        # adminで有意義のobj名を表示
        return self.title

    class Meta:
        # db中の表名前を設定：
        db_table = "todolist" 

        # adminでの表名前を設定：
        verbose_name = "Zwg's ToDoLists" 
        verbose_name_plural = verbose_name
