# Generated by Django 4.2.1 on 2023-07-19 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0007_eventdata_token_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventdata',
            name='event_desc',
            field=models.TextField(default='0'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='eventdata',
            name='flyer',
            field=models.ImageField(default='0', upload_to='Flyer'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='eventdata',
            name='text_chart',
            field=models.ImageField(default='0', upload_to='Text_Chart'),
            preserve_default=False,
        ),
    ]