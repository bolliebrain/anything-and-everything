# Generated by Django 3.2.23 on 2023-12-06 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myaande', '0002_comments'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=200)),
                ('datecommented', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Comments',
        ),
    ]