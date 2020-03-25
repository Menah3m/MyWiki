from django.db import models

class Category(models.Model):
    '''知识点领域分类'''
    category_name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.category_name

class Item(models.Model):
    '''具体的知识点'''
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default='')
    item_name = models.CharField(max_length=50)
    item_body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.item_name

