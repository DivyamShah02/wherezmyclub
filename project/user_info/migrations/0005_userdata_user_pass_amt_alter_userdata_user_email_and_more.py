# Generated by Django 4.2.1 on 2023-07-03 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_info', '0004_userdata_payment_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdata',
            name='user_pass_amt',
            field=models.CharField(default=0, max_length=10),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='user_email',
            field=models.EmailField(default=0, max_length=255),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='user_id',
            field=models.CharField(default=0, max_length=4),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='user_name',
            field=models.CharField(default=0, max_length=255),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='user_number',
            field=models.CharField(default=0, max_length=20),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='user_pass_qty',
            field=models.CharField(default=0, max_length=2),
        ),
    ]