# Generated by Django 5.1 on 2024-08-08 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IdealPrintshop', '0002_category_printshopservice_product_picture_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='category_picture',
            field=models.ImageField(blank=True, null=True, upload_to='service_category_pictures/'),
        ),
        migrations.AddField(
            model_name='printshoporder',
            name='payment_method',
            field=models.CharField(choices=[('cash', 'Cash'), ('mpesa', 'M-Pesa')], default='mpesa', max_length=5),
        ),
    ]
