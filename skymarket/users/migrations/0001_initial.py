# Generated by Django 3.2.6 on 2022-11-07 01:13

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('first_name', models.CharField(max_length=100, null=True, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=100, null=True, verbose_name='Фамилия')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, verbose_name='Телефон')),
                ('email', models.EmailField(max_length=50, unique=True, verbose_name='email address')),
                ('role', models.CharField(choices=[('user', 'Пользователь'), ('admin', 'Администратор')], default='user', max_length=5, verbose_name='Роль пользователя')),
                ('image', models.ImageField(blank=True, null=True, upload_to='django_media/users/', verbose_name='Фото пользователя')),
                ('is_active', models.BooleanField(default=True, null=True, verbose_name='Активность аккаунта')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
                'ordering': ('id',),
            },
        ),
    ]
