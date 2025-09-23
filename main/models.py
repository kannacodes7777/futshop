from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
import uuid
from django.contrib.auth.models import User

BRAND_CHOICES = [('nikey', 'Nikey'), ('adidas', 'Adidas'), ('puma', 'Puma'), ('reebok', 'Reebok')]
CATEGORY_CHOICES = [('topwear', 'Topwear'), ('bottomwear', 'Bottomwear'), ('shoes', 'Shoes'), ('accessories', 'Accessories')]

class Brand(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField()
    price = models.IntegerField()
    description = models.TextField()
    thumbnail = models.URLField()
    category = models.CharField(max_length=100,choices=CATEGORY_CHOICES ,default='Uncategorized')
    is_featured = models.BooleanField(default=False)
    stock = models.PositiveIntegerField(default=0)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    rating = models.FloatField(
        validators=[MinValueValidator(0.0), MaxValueValidator(5.0)],
        default=0.0
    )
    brand = models.CharField(max_length=100, choices=BRAND_CHOICES, default='No Brand')

    def __str__(self):
        return self.name