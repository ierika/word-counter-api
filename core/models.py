from django.db import models


class TimestampAbstractModel(models.Model):
    """Common properties among all models"""
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
