# Generated by Django 3.1 on 2020-08-09 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0005_task_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='created_at',
            field=models.DateField(editable=False),
        ),
    ]