# Generated by Django 5.1 on 2024-09-05 12:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
        ('school', '0004_remove_course_course_picture_remove_course_name_and_more'),
        ('staff', '0003_printshopoperator_is_active_teacher_is_active_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PrintshopOperator',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='email',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='name',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='profile_picture',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='subject',
        ),
        migrations.AddField(
            model_name='teacher',
            name='courses',
            field=models.ManyToManyField(related_name='teachers', to='school.course'),
        ),
        migrations.AddField(
            model_name='teacher',
            name='user',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='teacher_profile', to='base.user'),
            preserve_default=False,
        ),
    ]
