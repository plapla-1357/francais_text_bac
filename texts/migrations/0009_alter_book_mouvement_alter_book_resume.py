# Generated by Django 4.0 on 2021-12-18 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('texts', '0008_alter_book_mouvement_alter_book_resume'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='mouvement',
            field=models.CharField(blank=True, default='', max_length=64),
        ),
        migrations.AlterField(
            model_name='book',
            name='resume',
            field=models.TextField(blank=True, default=''),
        ),
    ]