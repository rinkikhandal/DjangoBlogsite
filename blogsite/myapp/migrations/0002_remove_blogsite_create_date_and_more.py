# Generated by Django 4.0.4 on 2022-05-11 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogsite',
            name='create_date',
        ),
        migrations.AlterField(
            model_name='blogsite',
            name='publish_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='blogsite',
            name='update_date',
            field=models.DateField(auto_now=True),
        ),
    ]
