# Generated by Django 4.2.1 on 2023-06-27 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='is_used',
            field=models.BooleanField(default=False),
        ),
    ]
