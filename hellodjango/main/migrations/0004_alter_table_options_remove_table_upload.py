# Generated by Django 4.2.7 on 2024-02-18 12:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_table_upload'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='table',
            options={'verbose_name': 'Товар', 'verbose_name_plural': 'Товары'},
        ),
        migrations.RemoveField(
            model_name='table',
            name='upload',
        ),
    ]
