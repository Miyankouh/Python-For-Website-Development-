# Generated by Django 3.2 on 2022-07-01 07:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('transaction', '0002_auto_20220630_1247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='transaction_type',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Charge'), (2, 'Purchase'), (3, 'Transfer received'), (4, 'Transfer sent')], default=1),
        ),
        migrations.CreateModel(
            name='UserScore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.PositiveSmallIntegerField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TransferTransaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('received_transaction', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='received_transfers', to='transaction.transaction')),
                ('sender_transaction', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='sent_transfers', to='transaction.transaction')),
            ],
        ),
    ]