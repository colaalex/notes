from django.db import models


class Note(models.Model):
    title = models.CharField(max_length=240, default='', blank=True)
    content = models.TextField()
