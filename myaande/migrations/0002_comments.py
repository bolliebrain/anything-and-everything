# Generated by Django 3.2.23 on 2023-12-06 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myaande', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=200)),
                ('datecommented', models.DateField(auto_now_add=True, null=True)),
            ],
        ),
    ]
