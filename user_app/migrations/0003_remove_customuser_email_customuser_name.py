# Generated by Django 4.2.7 on 2023-12-09 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0002_customuser_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='email',
        ),
        migrations.AddField(
            model_name='customuser',
            name='name',
            field=models.CharField(blank=True, max_length=455, null=True),
        ),
    ]
