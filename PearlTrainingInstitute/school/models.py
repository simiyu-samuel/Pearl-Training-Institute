from django.db import models
from base.models import User
from datetime import datetime

class CourseCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name


class Course(models.Model):
    course_image = models.ImageField(
        upload_to='courses/', null=True, blank=True)
    course_code = models.CharField(max_length=20, unique=True, blank=True)
    name = models.CharField(max_length=255)
    category = models.ForeignKey(CourseCategory, on_delete=models.CASCADE)
    description = models.TextField()
    duration = models.CharField(max_length=50)
    fee = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.course_code:
            year = datetime.now().year
            self.course_code = f"{
                self.category.name[:2].upper()}/{self.name[:2].upper()}/{year}"
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title


class Enrollment(models.Model):
    student = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='enrollments')
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name='enrollments')
    enrolled_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.username} enrolled in {self.course.title}"


class Payment(models.Model):
    PAYMENT_METHODS = [
        ('mpesa', 'Mpesa'),
        ('cash', 'Cash'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    method = models.CharField(max_length=10, choices=PAYMENT_METHODS)
    transaction_id = models.CharField(
        max_length=100, unique=True, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.method} - {self.amount}"
