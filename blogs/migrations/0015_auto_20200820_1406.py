# Generated by Django 3.1 on 2020-08-20 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0014_posts_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='default.jpg', height_field=400, upload_to='profile_pics', width_field=400),
        ),
    ]
