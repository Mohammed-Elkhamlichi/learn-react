# Generated by Django 4.0 on 2021-12-20 15:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_alter_todo_options_todo_completed'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='todo',
            options={'ordering': ['-updated']},
        ),
    ]