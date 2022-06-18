# Generated by Django 3.2 on 2022-06-18 09:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0002_producttype_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='producttype',
            name='created_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='producttype',
            name='modified_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
