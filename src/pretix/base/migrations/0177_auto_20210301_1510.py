# Generated by Django 3.0.10 on 2021-03-01 15:10

import jsonfallback.fields
import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pretixbase', '0176_auto_20210205_1512'),
    ]

    operations = [
        migrations.AddField(
            model_name='waitinglistentry',
            name='name_cached',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='waitinglistentry',
            name='name_parts',
            field=jsonfallback.fields.FallbackJSONField(default=dict),
        ),
        migrations.AddField(
            model_name='waitinglistentry',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, null=True, region=None),
        ),
    ]
