# Generated by Django 3.2.9 on 2021-12-16 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('texts', '0004_auto_20211216_1922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='date',
            field=models.IntegerField(),
        ),
    ]