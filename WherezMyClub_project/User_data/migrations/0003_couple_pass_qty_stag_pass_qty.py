# Generated by Django 4.2.1 on 2023-07-19 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User_data', '0002_couple_event_id_stag_event_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='couple',
            name='pass_qty',
            field=models.CharField(default='0', max_length=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='stag',
            name='pass_qty',
            field=models.CharField(default=1, max_length=5),
            preserve_default=False,
        ),
    ]
