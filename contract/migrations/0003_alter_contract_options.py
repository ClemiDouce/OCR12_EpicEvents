# Generated by Django 3.2.9 on 2021-11-09 09:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contract', '0002_contract_salecontact'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contract',
            options={'ordering': ['dateCreated'], 'verbose_name': 'Contract', 'verbose_name_plural': 'Contracts'},
        ),
    ]
