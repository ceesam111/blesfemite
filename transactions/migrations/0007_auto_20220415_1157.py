# Generated by Django 3.0.8 on 2022-04-15 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0006_auto_20220415_1119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='withdrawal',
            name='phone_number',
            field=models.IntegerField(blank=True),
        ),
    ]
