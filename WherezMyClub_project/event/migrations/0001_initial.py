# Generated by Django 4.2.1 on 2023-07-16 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EventData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('club_name', models.CharField(max_length=255)),
                ('hosts', models.CharField(max_length=255)),
                ('collaborater', models.CharField(max_length=255)),
                ('event_name', models.CharField(max_length=255)),
                ('event_venue', models.CharField(max_length=255)),
                ('event_date', models.CharField(max_length=100)),
                ('event_time', models.CharField(max_length=100)),
                ('free_gl', models.BooleanField(default=False)),
                ('paid_gl', models.BooleanField(default=False)),
                ('pass_price', models.CharField(default=0, max_length=10)),
                ('token_price', models.CharField(default=0, max_length=10)),
                ('gt_1', models.CharField(default='Null', max_length=255)),
                ('gt_2', models.CharField(default='Null', max_length=255)),
                ('gt_3', models.CharField(default='Null', max_length=255)),
                ('gt_4', models.CharField(default='Null', max_length=255)),
                ('gt_5', models.CharField(default='Null', max_length=255)),
                ('pt1_head', models.CharField(default='Null', max_length=50)),
                ('pt1_value', models.CharField(default='Null', max_length=50)),
                ('pt2_head', models.CharField(default='Null', max_length=50)),
                ('pt2_value', models.CharField(default='Null', max_length=50)),
                ('pt3_head', models.CharField(default='Null', max_length=50)),
                ('pt3_value', models.CharField(default='Null', max_length=50)),
                ('pt4_head', models.CharField(default='Null', max_length=50)),
                ('pt4_value', models.CharField(default='Null', max_length=50)),
                ('pt5_head', models.CharField(default='Null', max_length=50)),
                ('pt5_value', models.CharField(default='Null', max_length=50)),
                ('pt6_head', models.CharField(default='Null', max_length=50)),
                ('pt6_value', models.CharField(default='Null', max_length=50)),
            ],
        ),
    ]