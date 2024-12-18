# Generated by Django 5.1.3 on 2024-11-07 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event_booking', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='tickets_sold',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='event',
            name='total_tickets',
            field=models.IntegerField(default=100),
        ),
        migrations.AlterField(
            model_name='eventbooking',
            name='total_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
        ),
    ]