# Generated by Django 3.0.8 on 2020-08-01 09:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='created_date',
            new_name='create_date',
        ),
    ]
