# Generated by Django 4.2.2 on 2023-06-29 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_hostelpage_homepage_address_homepage_capacity_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='name',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
