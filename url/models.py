from django.db import models


class Url(models.Model):
    url = models.CharField(
        max_length=512, null=True, blank=True, verbose_name='URL')

    def __str__(self):
        return self.url
