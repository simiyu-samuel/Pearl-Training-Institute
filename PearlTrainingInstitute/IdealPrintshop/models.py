from django.db import models


class Category(models.Model):
    category_picture = models.ImageField(
        upload_to='service_category_pictures/', null=True, blank=True)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class PrintshopService(models.Model):
    product_picture = models.ImageField(
        upload_to='service_pictures/', null=True, blank=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='services', null=True, blank=True)

    def __str__(self):
        return self.name


class PrintshopOrder(models.Model):
    PAYMENT_METHOD_CHOICES = [
        ('cash', 'Cash'),
        ('mpesa', 'M-Pesa')
    ]

    service = models.ForeignKey(PrintshopService, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=100)
    customer_email = models.EmailField()
    details = models.TextField()
    payment_method = models.CharField(default='mpesa',
        max_length=5, choices=PAYMENT_METHOD_CHOICES)

    def __str__(self):
        return self.customer_name
