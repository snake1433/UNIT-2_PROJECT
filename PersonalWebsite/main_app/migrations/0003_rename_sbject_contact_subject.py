# Generated by Django 4.2.1 on 2023-06-06 11:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_contact'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='sbject',
            new_name='subject',
        ),
    ]