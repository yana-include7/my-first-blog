# Generated by Django 3.0.6 on 2020-06-15 14:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='post',
            name='profile_image',
            field=models.ImageField(default='img/9.png', upload_to='img'),
        ),
        migrations.AlterField(
            model_name='post',
            name='published_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
