# Generated by Django 3.0.4 on 2020-04-03 09:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo_list', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Task',
            new_name='List',
        ),
    ]
