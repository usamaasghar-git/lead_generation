from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Buyer(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    current_address = models.TextField()
    area_zip_code = models.CharField(max_length=10)
    email = models.EmailField(unique=True)  # Email field is unique for each Buyer instance
    budget = models.DecimalField(max_digits=10, decimal_places=2)

class Seller(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    current_address = models.TextField()
    area_zip_code = models.CharField(max_length=10)
    email = models.EmailField(unique=True)  # Email field is unique for each Seller instance
    budget = models.DecimalField(max_digits=10, decimal_places=2)

class Realtor(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    current_address = models.TextField()
    area_zip_code = models.CharField(max_length=10)
    email = models.EmailField(unique=True)  # Email field is unique for each Realtor instance
    subscription = models.BooleanField(default=False)
    rating = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)

class Rent(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    current_address = models.TextField()
    area_zip_code = models.CharField(max_length=10)
    email = models.EmailField(unique=True)  # Email field is unique for each Rent instance
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    rent_type = models.CharField(max_length=255)  # New field for property type
    bedrooms = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(3)])
    min_price_range = models.IntegerField(
        validators=[
            MinValueValidator(0), 
            MaxValueValidator(100),
        ]
    )
    max_price_range = models.IntegerField(
        validators=[
            MinValueValidator(1), 
            MaxValueValidator(100),
        ]
    )

class Blog(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()