# Generated by Django 4.2.6 on 2023-11-08 13:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_rename_link_lin'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Lin',
            new_name='Link',
        ),
    ]
