# Generated by Django 4.0 on 2021-12-18 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('texts', '0007_alter_book_resume'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='mouvement',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='resume',
            field=models.TextField(blank=True, null=True),
        ),
    ]
