from django.db import models


class Item(models.Model):
    text = models.TextField(default='')
    list = models.ForeignKey('ItemList', on_delete=models.CASCADE, default=None)


class ItemList(models.Model):
    pass
