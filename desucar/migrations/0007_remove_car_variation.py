# Generated by Django 2.0 on 2018-02-03 08:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('desucar', '0006_remove_maker_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='variation',
        ),
    ]
