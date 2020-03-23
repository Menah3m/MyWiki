from django.db import models

class Category(models.Model):
    category_name = models.CharField(max_length=50)
    category_created = models.DateTimeField()
    category_creator = models.CharField(max_length=50)

    def __str__(self):
        return self.category_name

class Item(models.Model):
    item_name = models.CharField(max_length=50)
    item_body = models.TextField()
    item_created = models.DateTimeField()
    item_creator = models.CharField(max_length=50)

    def __str__(self):
        return self.item_name

