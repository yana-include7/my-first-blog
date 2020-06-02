# Generated by Django 3.0.6 on 2020-06-02 08:45

import blog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to=blog.models.get_image_path),
        ),
    ]