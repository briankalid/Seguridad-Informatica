# Generated by Django 3.2.8 on 2021-10-23 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_homework',
            name='id',
        ),
        migrations.AlterField(
            model_name='user_homework',
            name='name',
            field=models.CharField(max_length=60, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='user_homework',
            name='pswd',
            field=models.CharField(max_length=4),
        ),
    ]