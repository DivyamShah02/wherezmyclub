# Generated by Django 4.2.1 on 2023-07-16 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventdata',
            name='event_id',
            field=models.CharField(default='0', max_length=10),
            preserve_default=False,
        ),
    ]
