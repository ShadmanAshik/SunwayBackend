# Generated by Django 4.0.1 on 2022-01-18 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AgentDataForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agentType', models.CharField(max_length=200)),
                ('fName', models.CharField(max_length=200)),
                ('lName', models.CharField(max_length=200)),
                ('country', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=200)),
                ('websiteaddress', models.CharField(max_length=200)),
                ('bestway', models.CharField(max_length=200)),
                ('agentphoto', models.ImageField(upload_to='agentphotos')),
            ],
        ),
        migrations.CreateModel(
            name='Snippet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=None, max_length=10, null=True)),
                ('photo', models.FileField(default=None, null=True, upload_to='snippets')),
            ],
        ),
    ]