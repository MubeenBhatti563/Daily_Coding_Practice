from django.db import models

# Create your models here.
class ViewsetModel(models.Model):
    name = models.CharField(max_length=100, blank=False)
    quality = models.CharField(max_length=100, blank=False)
    quantity = models.IntegerField(blank=False)

    def __str__(self):
        return self.name