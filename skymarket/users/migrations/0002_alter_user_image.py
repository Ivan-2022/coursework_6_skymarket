# Generated by Django 3.2.6 on 2022-11-08 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='users/', verbose_name='Фото пользователя'),
        ),
    ]