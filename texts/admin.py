from django.contrib import admin

from texts.models import Text, Book, Sequence, Text_interpretation, Plan

# Register your models here.
admin.site.register(Text)
admin.site.register(Book)
admin.site.register(Sequence)
admin.site.register(Text_interpretation)
admin.site.register(Plan)