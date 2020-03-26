from django.db import models
from uuslug import slugify



class Category(models.Model):
    '''知识点领域分类'''
    category_name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    category_slug = models.SlugField(max_length=50, editable=False)

    def __str__(self):
        return self.category_name

    def save(self, *args, **kwargs):
        self.category_slug = slugify(self.category_name)
        super(Category,self).save(*args, **kwargs)

class Item(models.Model):
    '''具体的知识点'''
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default='')
    item_name = models.CharField(max_length=50)
    item_body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    item_slug = models.SlugField(max_length=50, editable=False)

    def save(self, *args, **kwargs):
        self.item_slug = slugify(self.item_name)
        super(Item,self).save(*args, **kwargs)


    def __str__(self):
        return self.item_name

