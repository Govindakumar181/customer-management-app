# Generated by Django 3.0.3 on 2020-10-16 08:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20201016_1237'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='data_created',
            new_name='date_created',
        ),
    ]