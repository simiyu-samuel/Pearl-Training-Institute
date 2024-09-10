from django.db import models
from base.models import User
from school.models import Course


class Teacher(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='teacher_profile')
    courses = models.ManyToManyField(Course, related_name='teachers')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username
