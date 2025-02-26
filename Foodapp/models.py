from django.db import models

# Create your models here.
class Item(models.Model):
    item_name = models.CharField(max_length = 100)
    item_desc = models.CharField(max_length = 100)
    price = models.IntegerField()
    item_image = models.URLField(default = "https://i.pinimg.com/1200x/e2/ae/e5/e2aee59c58c648664bb1dfa3b2ea1453.jpg")
