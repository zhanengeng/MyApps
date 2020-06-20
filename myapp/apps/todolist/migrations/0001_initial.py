# Generated by Django 2.2 on 2020-06-20 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyToDoList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='追加時間')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新時間')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='削除済')),
                ('title', models.CharField(max_length=255, verbose_name='タイトル')),
                ('contents', models.TextField(verbose_name='詳細')),
                ('deadline', models.DateTimeField(verbose_name='締切')),
                ('done', models.BooleanField(default=False, verbose_name='完成')),
            ],
            options={
                'verbose_name': 'ToDoList',
                'verbose_name_plural': 'ToDoList',
                'db_table': 'todolist',
            },
        ),
    ]
