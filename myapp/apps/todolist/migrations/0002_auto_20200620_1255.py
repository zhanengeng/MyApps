# Generated by Django 2.2 on 2020-06-20 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mytodolist',
            name='deadline',
            field=models.DateField(verbose_name='締切'),
        ),
    ]