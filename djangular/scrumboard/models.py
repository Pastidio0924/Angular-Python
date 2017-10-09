from django.db import models


# Create your models here.

class List(models.Model):
    name = models.CharField(max_length=50)
    def _str_(self):
        return "List:{}".format(self.name)


class Card(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    list = models.ForeignKey(List, related_name="card")
    story_points = models.IntegerField(null=True, blank=True)
    business_value = models.IntegerField(null=True, blank=True)

def _str_(self):
    return "Card:{}".format(self.title)
