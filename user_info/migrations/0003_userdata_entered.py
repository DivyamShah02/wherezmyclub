# Generated by Django 4.2.1 on 2023-07-01 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_info', '0002_userdata_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdata',
            name='entered',
            field=models.BooleanField(default=False),
        ),
    ]
