# Generated by Django 4.2.7 on 2023-11-22 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_app', '0008_order_created_at_order_updated_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='count',
        ),
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[(1, 'Buyurtma berildi'), (2, 'Yetkazildi'), (3, 'Bekor qilindi')], default=1, max_length=255),
        ),
    ]
