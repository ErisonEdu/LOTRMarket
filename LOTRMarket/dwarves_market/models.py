from django.db import models

class DwarvenItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    value = models.IntegerField()

    def __str__(self):
        return self.name

class DwarvenWeapon(models.Model):
    name = models.CharField(max_length=100)
    categories = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    value = models.IntegerField()

    def __str__(self):
        return self.description