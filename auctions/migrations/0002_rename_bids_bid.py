# Generated by Django 4.1 on 2022-08-27 22:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_alter_playercard_portfolio'),
        ('auctions', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Bids',
            new_name='Bid',
        ),
    ]
