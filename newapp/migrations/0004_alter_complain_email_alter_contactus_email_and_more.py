# Generated by Django 5.0 on 2024-01-29 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0003_alter_customuser_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complain',
            name='email',
            field=models.EmailField(max_length=100),
        ),
        migrations.AlterField(
            model_name='contactus',
            name='email',
            field=models.EmailField(max_length=100),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='email',
            field=models.EmailField(max_length=100),
        ),
    ]
