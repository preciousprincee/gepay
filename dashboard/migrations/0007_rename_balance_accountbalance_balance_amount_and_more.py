# Generated by Django 4.2.4 on 2024-03-18 15:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dashboard', '0006_accountbalance_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='accountbalance',
            old_name='balance',
            new_name='balance_amount',
        ),
        migrations.RemoveField(
            model_name='accountbalance',
            name='transactions',
        ),
        migrations.AddField(
            model_name='transaction',
            name='amount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='accountbalance',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='account_balance', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='ProfilePicture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='profile_pictures')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile_picture', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
