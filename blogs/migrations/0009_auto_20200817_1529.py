# Generated by Django 3.1 on 2020-08-17 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0008_auto_20200816_2056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='occupation',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]