# Generated by Django 4.2.1 on 2023-07-21 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0012_eventdata_event_date_alt_eventdata_event_time_alt'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventdata',
            name='max_pass',
            field=models.CharField(default=15, max_length=10),
        ),
    ]
