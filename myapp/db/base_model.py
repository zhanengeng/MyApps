from django.db import models
# from model_utils.models import SoftDeletableModel # 启用逻辑删除，需要安装model_utils包？有待验证

class BaseModel(models.Model):
# class BaseModel(SoftDeletableModel):
    '''模型抽象基类'''
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="追加時間")
    update_time = models.DateTimeField(auto_now=True, verbose_name="更新時間")
    is_deleted = models.BooleanField(default=False, verbose_name="削除済") 

    class Meta:
        # 说明这是一个抽象模型类
        abstract = True