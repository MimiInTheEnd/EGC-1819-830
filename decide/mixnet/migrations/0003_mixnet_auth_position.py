# Generated by Django 2.0 on 2018-04-04 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mixnet', '0002_auto_20180216_1617'),
    ]

    operations = [
        migrations.AddField(
            model_name='mixnet',
            name='auth_position',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
