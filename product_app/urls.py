from django.urls import path

from .views import CategoryList, ProductList, OrderListCreateView, \
    OrderDetailView, UserOrdersAPIView, OrderUpdateView, ProductDetailAPIView

urlpatterns = [
    path('category/', CategoryList.as_view()),
    path('products/', ProductList.as_view()),
    path('products/<int:product_id>/', ProductDetailAPIView.as_view(), name='product-detail'),

    path('orders/', OrderListCreateView.as_view(), name='order-list-create'),
    path('user-orders/<int:user_id>/', UserOrdersAPIView.as_view(), name='user-orders'),
    path('orders/<int:pk>/', OrderDetailView.as_view(), name='order-detail'),
    path('order-update/<int:pk>/', OrderUpdateView.as_view(), name='order-update'),
]