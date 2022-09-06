# Generated by Django 4.1 on 2022-09-06 10:38

from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', django_countries.fields.CountryField(max_length=2)),
            ],
            options={
                'verbose_name': 'Country',
                'verbose_name_plural': 'Countries',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('position', models.CharField(max_length=255)),
                ('date_of_birth', models.DateField()),
                ('jersey_number', models.CharField(max_length=10)),
                ('slug', models.SlugField(blank=True, help_text='Label for URL configuration', max_length=55, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PlayerCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField(default=0)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='uploads/cards')),
                ('index', models.IntegerField(blank=True, null=True)),
                ('slug', models.SlugField(blank=True, max_length=55, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Rarity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Rarity',
                'verbose_name_plural': 'Rarities',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
                ('slug', models.SlugField(blank=True, help_text='Label for URL configuration', max_length=55, null=True, unique=True)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.country')),
            ],
            options={
                'ordering': ['year'],
            },
        ),
    ]
