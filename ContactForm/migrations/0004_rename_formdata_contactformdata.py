# Generated by Django 4.0 on 2021-12-28 16:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ContactForm', '0003_rename_counsellingmode_formdata_counselingmode'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='FormData',
            new_name='ContactFormData',
        ),
    ]
