# Generated by Django 4.0 on 2021-12-19 19:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('texts', '0011_rename_titre_book_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='tumbnail',
            new_name='thumbnail',
        ),
    ]