from django.contrib.auth.models import AbstractUser
from django.core.validators import EmailValidator, MinLengthValidator
from django.db import models

class CustomUser(AbstractUser):
    first_name = models.CharField(
        max_length=30,
        verbose_name='First Name',
        validators=[MinLengthValidator(limit_value=2)]
    )
    last_name = models.CharField(
        max_length=30,
        verbose_name='Last Name',
        validators=[MinLengthValidator(limit_value=2)]
    )
    ADMIN = 'admin'
    REALTOR = 'realtor'
    CUSTOMER = 'customer'
    
    ROLE_CHOICES = [
        (ADMIN, 'Admin'),
        (REALTOR, 'Realtor'),
        (CUSTOMER, 'Customer'),
    ]

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default=CUSTOMER,
        verbose_name='Role',
    )
    email = models.EmailField(unique=True, validators=[EmailValidator(message='Enter a valid email address.')])

    # Add unique related_name attributes to avoid clashes
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_groups',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    def __str__(self):
        return self.username
