from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=128)
    
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        
    def to_json(self):
        return {
            'name': self.name
        }

class Product(models.Model):
    name = models.CharField(max_length=256)
    price = models.FloatField()
    description = models.TextField(null=True, blank=True)
    count = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    def to_json(self):
        return {
            'id' : self.id,
            'name': self.name,
            'price': self.price,
            'description': self.description,
            'count': self.count,
            'is_active': self.is_active  
        }