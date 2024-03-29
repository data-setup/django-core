from django.db import models

def get_default_category():
    # Assuming there's always at least one category and its id is 1
    return Category.objects.get_or_create(name='Default')[0].id

class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE, default=get_default_category)
    # Consider adding an ImageField or FileField for product images
    
    def __str__(self):
        return self.name
