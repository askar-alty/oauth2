# Generated by Django 2.1.5 on 2019-02-01 08:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.OAUTH2_PROVIDER_APPLICATION_MODEL),
        ('core', '0002_auto_20190131_1322'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('applications', models.ManyToManyField(to=settings.OAUTH2_PROVIDER_APPLICATION_MODEL, verbose_name='Приложения')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'профиль',
                'verbose_name_plural': 'профили',
            },
        ),
    ]