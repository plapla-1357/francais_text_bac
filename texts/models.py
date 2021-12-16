from django.db import models
from django.core.validators import MaxValueValidator


class Text(models.Model):
    name = models.CharField(max_length=128)
    titre = models.CharField(max_length=128)
    chapter = models.IntegerField()
    partie = models.IntegerField()
    text = models.TextField()

    def __str__(self):
        return self.name


class Book(models.Model):
    titre = models.CharField(max_length=128)
    date = models.PositiveIntegerField(validators=[MaxValueValidator(2022)])
    author = models.CharField(max_length=128)
    tumbnail = models.ImageField(upload_to="Image", blank=True, null=True)

    def __str__(self):
        return self.titre
