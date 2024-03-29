# Generated by Django 5.0 on 2024-01-16 11:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('brand', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100, unique=True)),
                ('Price', models.DecimalField(decimal_places=5, max_digits=10)),
                ('Quantity', models.IntegerField()),
                ('Description', models.TextField()),
                ('ReleaseDate', models.DateField()),
                ('slug', models.SlugField(blank=True, max_length=100, null=True, unique=True)),
                ('BrandName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='brand.brandmodel')),
            ],
        ),
        migrations.CreateModel(
            name='CommentsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Body', models.TextField()),
                ('CreatedDate', models.DateField(auto_now_add=True)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='car.carmodel')),
            ],
        ),
    ]
