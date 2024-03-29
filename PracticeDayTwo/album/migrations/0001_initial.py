# Generated by Django 5.0 on 2024-01-14 06:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('musician', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AlbumModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=200)),
                ('Rating', models.CharField(choices=[(1, 'One'), (2, 'Two'), (3, 'Three'), (4, 'Four'), (5, 'Five')], max_length=10)),
                ('ReleaseDate', models.DateField()),
                ('MusicianName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='musician', to='musician.musicianmodel')),
            ],
        ),
    ]
