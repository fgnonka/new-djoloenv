# Generated by Django 4.1 on 2022-08-27 20:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_alter_djolowinuser_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playercard',
            name='portfolio',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.portfolio'),
        ),
    ]