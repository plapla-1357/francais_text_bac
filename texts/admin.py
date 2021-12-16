from django.contrib import admin

from texts.models import Text, Book
# Register your models here.
admin.site.register(Text)
admin.site.register(Book)
