from django.db import models
from django.urls import reverse


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)


from django.db import models


class Category(models.Model):
    name_cat = models.CharField(max_length=250)

    def __str__(self):
        return self.name_cat


class Subcategory(models.Model):
    name_subcat = models.CharField(max_length=250)
    id_subcat = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.name_subcat

class GeneralmenuItem(models.Model):
    order = models.ForeignKey("menus.Generalmenu", on_delete=models.CASCADE, verbose_name="Generalmenu")
    subcat = models.ForeignKey(Subcategory, on_delete=models.CASCADE, verbose_name='subcat')



    def __str__(self):
        return str(self.subcat)

class Generalmenu(models.Model):
    cat = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='category')
    id_cat = models.PositiveIntegerField(default=0)

    def __str__(self):
        return str(self.cat)



