# Generated by Django 4.1.10 on 2023-09-05 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_alter_applyjob_status_alter_job_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applyjob',
            name='status',
            field=models.CharField(choices=[('Declined', 'Declined'), ('Accepted', 'Accepted'), ('Pending', 'Pending')], max_length=50),
        ),
    ]
