# Generated by Django 3.2.5 on 2022-05-16 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('txApp', '0002_auto_20220516_2137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transactionsinfo',
            name='Description',
            field=models.TextField(null=True),
        ),
    ]
