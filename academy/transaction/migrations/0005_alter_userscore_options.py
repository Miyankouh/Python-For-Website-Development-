# Generated by Django 3.2 on 2022-07-02 09:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0004_alter_userscore_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userscore',
            options={'permissions': [('has_score_permission', 'user has score permission')]},
        ),
    ]