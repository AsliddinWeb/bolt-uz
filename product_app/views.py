from rest_framework.decorators import api_view, permission_classes
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from rest_framework.views import APIView
from rest_framework import status

from .models import Category, Product, Order
from .serializers import CategorySerializer, ProductSerializer, UserSerializer, \
    OrderSerializer, OrderCreateSerializer, OrderSerializer1

class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]

class ProductList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

class ProductDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, product_id, format=None):
        try:
            product_id = int(product_id)
            product = Product.objects.get(id=product_id)
            serializer = ProductSerializer(product)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except ValueError:
            return Response(status=status.HTTP_404_NOT_FOUND)

class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return OrderCreateSerializer
        return OrderSerializer

class OrderDetailView(generics.RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

class UserOrdersAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, user_id, format=None):
        try:
            user_id = int(user_id)
            orders = Order.objects.filter(user=user_id)
            serializer = OrderSerializer(orders, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except ValueError:
            return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getProfile(request):
    user = request.user
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)

class OrderUpdateView(APIView):
    permission_classes = [IsAuthenticated]
    def patch(self, request, *args, **kwargs):
        # Buyurtma id sini olish (URL parametri)
        order_id = kwargs.get('pk')
        try:
            order = Order.objects.get(id=order_id)
        except Order.DoesNotExist:
            return Response({"error": "Buyurtma topilmadi"}, status=status.HTTP_404_NOT_FOUND)

        # Buyurtma holatini o'zgartirish
        new_status = request.data.get('status')
        if new_status == '1' or new_status == '2' or new_status == '3':
            order.status = new_status
            order.save()
            serializer = OrderSerializer(order)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Status xato kiritildi!"}, status=status.HTTP_400_BAD_REQUEST)