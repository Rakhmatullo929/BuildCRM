# Generated by Django 4.1.5 on 2023-05-10 15:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0002_client_team'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='client',
            options={'ordering': ('name',)},
        ),
    ]