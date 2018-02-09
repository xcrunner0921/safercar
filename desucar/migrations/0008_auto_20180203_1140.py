# Generated by Django 2.0 on 2018-02-03 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('desucar', '0007_remove_car_variation'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='code',
            field=models.CharField(default='', max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='car',
            name='make_end',
            field=models.DateField(default='9999-12-31'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='car',
            name='make_start',
            field=models.DateField(default='9999-12-31'),
            preserve_default=False,
        ),
    ]