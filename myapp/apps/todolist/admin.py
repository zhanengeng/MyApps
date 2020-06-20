from django.contrib import admin
from .models import MyToDoList

# Register your models here.

# admin.site.register(MyToDoList) # モデルをadminに登録

@admin.register(MyToDoList)
class MyToDoListAdmin(admin.ModelAdmin):
    list_display = ["title", "create_time","update_time","deadline","done","is_deleted"]
