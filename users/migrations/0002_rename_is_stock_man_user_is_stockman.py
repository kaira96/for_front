# Generated by Django 4.1.1 on 2022-10-03 17:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='is_stock_man',
            new_name='is_stockman',
        ),
    ]
