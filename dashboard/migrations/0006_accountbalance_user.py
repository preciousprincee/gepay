# Generated by Django 4.2.4 on 2024-02-29 10:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dashboard', '0005_remove_accountbalance_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='accountbalance',
            name='user',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='account_balance', to=settings.AUTH_USER_MODEL),
        ),
    ]
