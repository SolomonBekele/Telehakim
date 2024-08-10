# Generated by Django 4.2.1 on 2023-06-15 18:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_delete_appointment'),
        ('appointment', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=False)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.doctor')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.patient')),
                ('schedule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appointment.workingday')),
            ],
        ),
        migrations.DeleteModel(
            name='Booking',
        ),
    ]
