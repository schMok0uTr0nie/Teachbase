# Generated by Django 4.1.7 on 2023-03-24 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='duration',
            field=models.IntegerField(help_text='Duration in sec.', null=True),
        ),
    ]