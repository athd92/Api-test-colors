from django.db import models


class Colors(models.Model):
    '''Class defined for the colors infos'''
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    pantone_value = models.CharField(max_length=100)
    year = models.CharField(max_length=100)

    def __str__(self):
        return self.name
