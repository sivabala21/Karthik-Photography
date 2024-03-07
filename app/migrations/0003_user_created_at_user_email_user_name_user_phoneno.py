# Generated by Django 5.0.2 on 2024-03-07 12:16

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_photos_user_delete_form'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.EmailField(default='2024-02-25 15:30:20.123456', max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='name',
            field=models.CharField(default='siva', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='phoneno',
            field=models.IntegerField(default='9876764565'),
            preserve_default=False,
        ),
    ]
