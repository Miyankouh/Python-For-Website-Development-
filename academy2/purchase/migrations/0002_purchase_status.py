# Generated by Django 3.2 on 2022-07-19 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchase', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='status',
            field=models.SmallIntegerField(choices=[(10, 'Paid'), (-10, 'Not paid')], default=-10),
        ),
    ]
