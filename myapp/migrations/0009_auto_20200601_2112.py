# Generated by Django 3.0.6 on 2020-06-02 04:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_profile_rol3'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='rol3',
            new_name='role',
        ),
    ]
