# Generated by Django 3.2.16 on 2022-12-24 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_logs_generated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logs_generated',
            name='date',
            field=models.DateTimeField(default='20:21:42'),
        ),
    ]