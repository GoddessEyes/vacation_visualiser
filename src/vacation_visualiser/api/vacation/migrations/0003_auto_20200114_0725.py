# Generated by Django 3.0.2 on 2020-01-13 21:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vacation', '0002_auto_20200111_0425'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vacation',
            options={'verbose_name': 'Отпуск', 'verbose_name_plural': 'Отпуска'},
        ),
    ]