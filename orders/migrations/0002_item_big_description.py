# Generated by Django 3.0.8 on 2020-07-19 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='big_description',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
    ]
