# from django.contrib.auth.models import User
from user_app.models import CustomUser as User
from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField
from .models import Category, Product, Order, OrderItem

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class ProductSerializer(ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = Product
        fields = '__all__'

class OrderItemSerializer(ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = OrderItem
        fields = '__all__'

class OrderSerializer(ModelSerializer):
    products = ProductSerializer(many=True)
    total_quantity = SerializerMethodField()
    user = UserSerializer(many=False)

    class Meta:
        model = Order
        fields = '__all__'

    def get_total_quantity(self, obj):
        return obj.total_quantity

class OrderItemCreateSerializer(ModelSerializer):
    product = PrimaryKeyRelatedField(queryset=Product.objects.all(), write_only=True)

    class Meta:
        model = OrderItem
        fields = ['product', 'quantity']

class OrderCreateSerializer(ModelSerializer):
    products = OrderItemCreateSerializer(many=True)

    class Meta:
        model = Order
        fields = "__all__"

    def create(self, validated_data):
        products_data = validated_data.pop('products')
        user_data = validated_data.pop('user', None)

        # Create Order instance
        order = Order.objects.create(user=user_data, **validated_data)

        for product_data in products_data:
            product_instance = product_data.pop('product')
            order_item_data = {'order': order, 'product': product_instance, **product_data}

            # Create OrderItem instance
            OrderItem.objects.create(**order_item_data)

        return order



class OrderSerializer1(ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'