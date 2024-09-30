from django.db import models
from django.template.defaultfilters import slugify


class Phone(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField(null=True)
    image = models.ImageField(blank=True)
    release_date = models.DateField(auto_now=True)
    lte_exists = models.BooleanField(default=False)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)

        super(Phone, self).save(*args, **kwargs)