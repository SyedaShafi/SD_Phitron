# Generated by Django 5.0.3 on 2024-04-02 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_remove_categorymodel_tasks'),
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='taskmodel',
            name='category',
            field=models.ManyToManyField(to='category.categorymodel'),
        ),
    ]
