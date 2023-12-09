from django.db import models
# from django.contrib.auth.models import User
from user_app.models import CustomUser as User

class Category(models.Model):
    name = models.CharField(max_length=255)
    caption = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Kategoriyalar"

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    body = models.TextField(null=True, blank=True)
    razmer = models.CharField(max_length=455, null=True, blank=True)
    image = models.ImageField(upload_to='products', null=True, blank=True)
    filter = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Maxsulotlar"

STATUS = (
    ('1', 'Buyurtma berildi'),
    ('2', 'Yetkazildi'),
    ('3', 'Bekor qilindi'),
)
class Order(models.Model):
    products = models.ManyToManyField(Product, through='OrderItem')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    status = models.CharField(max_length=255, choices=STATUS)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def total_quantity(self):
        return sum(item.quantity for item in self.orderitem_set.all())

    def __str__(self):
        return f"Order {self.id}"

    class Meta:
        verbose_name_plural = "Buyurtmalar"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} {self.product.name} in Order {self.order.id}"

    class Meta:
        verbose_name_plural = "Buyurtma berilgan maxsulotlar"

