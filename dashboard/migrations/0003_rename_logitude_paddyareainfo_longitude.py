# Generated by Django 3.2.7 on 2021-12-11 19:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_auto_20211209_1749'),
    ]

    operations = [
        migrations.RenameField(
            model_name='paddyareainfo',
            old_name='logitude',
            new_name='longitude',
        ),
    ]
