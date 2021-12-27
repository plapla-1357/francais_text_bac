from django.db import models
from django.core.validators import MaxValueValidator
from django.template.defaultfilters import slugify


class SeparatedValuesField(models.TextField):
    def __init__(self, separator=",", final_type=None, *args, **kwargs):
        self.separator = separator
        self.final_type = final_type
        super(SeparatedValuesField, self).__init__(*args, **kwargs)

    def to_python(self, value):
        print("to python called")
        if not value: return
        if isinstance(value, list):
            return value
        return value.split(self.separator)

    def from_db_value(self, value, expression, connection):
        print("from_db_value called")
        if not value:
            return
        if self.final_type != None:
            return [self.final_type(i) for i in value.split(self.separator)]
        else:
            return value.split(self.separator)

    def get_db_prep_value(self, value, connection, prepared=False):
        value = super().get_db_prep_value(value, connection, prepared)
        if not value:
            return
        assert (isinstance(value, list) or isinstance(value, tuple))
        # renvoye une assertion error si ce n'est pas une list ou un tuple
        return self.separator.join(value)

    def value_to_string(self, obj):
        value = self._get_val_from_obj(obj)
        return self.get_db_prep_value(value)

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        # Only include kwarg if it's not the default
        if self.separator != ",":
            kwargs['separator'] = self.separator
        if self.final_type != None:
            kwargs['final_type'] = self.final_type
        return name, path, args, kwargs


class Sequence(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=128)
    slug_title = models.SlugField(unique=True, blank=True, editable=False)

    date = models.PositiveIntegerField(validators=[MaxValueValidator(2022)])
    author = models.CharField(max_length=128)
    mouvement = models.CharField(max_length=64, blank=True, default="")

    resume = models.TextField(blank=True, default="")
    thumbnail = models.ImageField(upload_to="Image",
                                  blank=True,
                                  null=True)

    sequence = models.ForeignKey(Sequence,
                                 on_delete=models.DO_NOTHING,
                                 null=True)

    def save(self, *arg, **kwargs):
        self.slug_title = slugify(self.title)
        super(Book, self).save(*arg, **kwargs)

    def __str__(self):
        return self.title


class Text(models.Model):
    name = models.CharField(max_length=128)
    text_id = models.PositiveIntegerField(default=1)
    slug_name = models.SlugField(unique=True, blank=True, editable=False)
    book = models.ForeignKey(Book, default=None, on_delete=models.CASCADE)
    chapter = models.IntegerField()
    partie = models.IntegerField()
    text = SeparatedValuesField("<br>")

    sequence = models.ForeignKey(Sequence,
                                 on_delete=models.DO_NOTHING,
                                 null=True)

    def save(self, *arg, **kwargs):
        self.slug_name = slugify(self.name)
        super(Text, self).save(*arg, **kwargs)

    def __str__(self):
        return self.name


class Text_interpretation(models.Model):
    Text = models.ForeignKey(Text, on_delete=models.CASCADE)
    extrait = models.CharField(max_length=512, blank=True)
    line = models.CharField(max_length=64, blank=True)

    outil = models.CharField(max_length=128, blank=True)
    choice_outil_type = (
        (1, "figure de style"),
        (2, "champs lexical"),
        (3, "poctuation"),
        (4, "temps"),
        (5, "tonalités"),
        (6, "autre")
    )
    outil_type = models.IntegerField(choices=choice_outil_type, blank=True)
    interpretation = models.TextField(blank=True)

    def __str__(self):
        return f" \"{self.Text.name}\" l-{self.line} [{dict(self.choice_outil_type)[self.outil_type]}] :\
         {self.interpretation[:50]} ..."
# TEXT INTERPRETATION
    # extrait
    # ligne
    # outils
    # interpretation

class Plan(models.Model):
    text = models.ForeignKey(Text, on_delete=models.CASCADE)
    partie_I = models.CharField(max_length=256)
    ligne_partie_I = SeparatedValuesField(final_type=int, editable=False, blank=True)
    partie_II = models.CharField(max_length=256, blank=True)
    ligne_partie_II = SeparatedValuesField(final_type=int, editable=False, blank=True)
    partie_III = models.CharField(max_length=256, blank=True)
    ligne_partie_III = SeparatedValuesField(final_type=int, editable=False, blank=True)
    partie_IV = models.CharField(max_length=256, blank=True)
    ligne_partie_IV = SeparatedValuesField(final_type=int, editable=False, blank=True)
    introduction = models.TextField(blank=True)
    conclusion = models.TextField(blank=True)
    ouverture = models.TextField(blank=True)



# todo de quoi stoker des auteur
# todo ajouter les info sur les text dans la database
# todo ajouter une table plan
