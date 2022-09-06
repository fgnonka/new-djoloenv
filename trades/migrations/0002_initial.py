# Generated by Django 4.1 on 2022-09-06 10:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('trades', '0001_initial'),
        ('base', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tradecard',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='ordercard',
            name='tradecard',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trades.tradecard'),
        ),
        migrations.AddField(
            model_name='order',
            name='buyer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='single_buyer', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='order',
            name='card',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trades.ordercard'),
        ),
        migrations.AddField(
            model_name='bundleorder',
            name='bundle',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trades.bundle'),
        ),
        migrations.AddField(
            model_name='bundleorder',
            name='buyer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bundle_buyer', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='bundle',
            name='cards',
            field=models.ManyToManyField(blank=True, related_name='bundle_cards', to='base.playercard'),
        ),
    ]
