# Generated by Django 4.1 on 2023-12-11 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0010_rename_vendorreview_reviewvendor'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviewvendor',
            name='vendor_code',
            field=models.CharField(blank=True, max_length=256),
        ),
        migrations.AddField(
            model_name='vendorrequest',
            name='vendor_code',
            field=models.CharField(blank=True, max_length=256),
        ),
    ]
