# Generated by Django 4.1.7 on 2023-04-15 05:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0008_remove_travertin_not_available_granit_is_available_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='granit',
            old_name='is_custom_order',
            new_name='order_only',
        ),
        migrations.RenameField(
            model_name='mramor',
            old_name='is_custom_order',
            new_name='order_only',
        ),
    ]
