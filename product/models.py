from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    featured = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['title']

    def __str__(self) -> str:
        return self.title

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    title = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    featured = models.BooleanField(default=False)
    discription = models.TextField(blank=True, null=True,)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    thumbnail = models.URLField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-id']

    def __str__(self) -> str:
        return self.title
    
class Slider(models.Model):
    title = models.CharField(max_length=50)
    title2 = models.CharField(max_length=50, default='Lookbook.')
    banner = models.ImageField(upload_to='banners')
    show = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.title2
