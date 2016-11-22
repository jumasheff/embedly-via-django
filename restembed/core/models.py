from django.db import models


class SavedEmbeds(models.Model):
    url = models.URLField()
    type = models.CharField(max_length=15)
    provider_url = models.URLField()
    provider_name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.TextField(null=True)
    html = models.TextField(null=True)
    width = models.IntegerField(null=True)
    thumbnail_url = models.URLField(null=True)
    thumbnail_width = models.IntegerField(null=True)
    thumbnail_height = models.IntegerField(null=True)
    author_url = models.URLField(null=True)
    author_name = models.CharField(max_length=100, null=True)
    version = models.DecimalField(max_digits=4, decimal_places=2)
