# Generated by Django 4.0 on 2021-12-19 18:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('texts', '0010_remove_text_titre_book_slug_title_text_book_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='titre',
            new_name='title',
        ),
    ]