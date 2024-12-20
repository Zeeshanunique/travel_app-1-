# Generated by Django 5.1.3 on 2024-11-07 07:08

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cab',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cab_type', models.CharField(max_length=50)),
                ('base_fare', models.DecimalField(decimal_places=2, max_digits=6)),
                ('per_km_rate', models.DecimalField(decimal_places=2, max_digits=4)),
            ],
        ),
        migrations.CreateModel(
            name='CabBooking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pickup_location', models.CharField(max_length=200)),
                ('drop_location', models.CharField(max_length=200)),
                ('pickup_time', models.DateTimeField()),
                ('estimated_fare', models.DecimalField(decimal_places=2, max_digits=8)),
                ('cab', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cab_booking.cab')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
