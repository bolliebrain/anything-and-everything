# Generated by Django 3.2.23 on 2023-12-14 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myaande', '0005_post_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
    ]
