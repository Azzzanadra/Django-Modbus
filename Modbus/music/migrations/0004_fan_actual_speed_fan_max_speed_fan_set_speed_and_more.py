# Generated by Django 5.0.2 on 2024-03-03 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0003_alter_fan_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='fan',
            name='actual_speed',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='fan',
            name='max_speed',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='fan',
            name='set_speed',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='fan',
            name='status',
            field=models.IntegerField(default=0),
        ),
    ]
