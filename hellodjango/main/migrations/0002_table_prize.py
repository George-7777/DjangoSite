# Generated by Django 4.2.7 on 2024-02-11 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='table',
            name='prize',
            field=models.IntegerField(default=0, verbose_name='Цена'),
            preserve_default=False,
        ),
    ]
