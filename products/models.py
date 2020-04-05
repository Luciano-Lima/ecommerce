from django.db import models
from django.urls import reverse

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200, unique=True, default='Category Name')
    description = models.TextField(blank=True, null=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True) 

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_url(self):
        return reverse('products_by_category', args=[self.slug])
    
    def __str__(self):
        return self.name
    


class Product(models.Model):
    name = models.CharField(max_length=200, unique=True, default='Product Name')
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    image = models.ImageField(upload_to='images', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    slug = models.SlugField(max_length=200, unique=True, null=True, blank=True)  

    def get_url(self):
        return reverse('product_detail', args=[self.category.slug, self.slug])
       
    def __str__(self):
        return self.name