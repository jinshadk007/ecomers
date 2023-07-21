from django.db import models
from django.urls import reverse
from home.models import Category


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=100, null=False, blank=False, unique=True)
    slug = models.SlugField(max_length=100, null=False, blank=False, unique=True)
    product_image = models.ImageField(upload_to="photos/products", null=False, blank=False)
    description = models.TextField()
    stock = models.IntegerField()
    is_available = models.BooleanField(default=True)
    original_price = models.IntegerField()
    offer_price = models.IntegerField()
    trending = models.BooleanField()
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def get_url(self):
        return reverse('product_detail', args=[self.category.slug, self.slug])

    def __str__(self):
        return self.product_name


class search_else(models.Model):
    msg = models.CharField(max_length=200 ,blank=True)
    img = models.ImageField(upload_to="product", )

    def __str__(self):
        return '{}'.format(self.msg)
