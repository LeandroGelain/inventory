# Generated by Django 2.0.2 on 2018-03-05 21:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_auto_20180305_2127'),
    ]

    operations = [
        migrations.RenameField(
            model_name='consumin',
            old_name='id',
            new_name='sl_no',
        ),
        migrations.RenameField(
            model_name='issuein',
            old_name='id',
            new_name='sl_no',
        ),
    ]
