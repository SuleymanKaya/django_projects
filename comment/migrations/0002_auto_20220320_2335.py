# Generated by Django 3.2.9 on 2022-03-20 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentmodel',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='commentmodel',
            name='modified',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
