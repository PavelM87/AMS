from django.urls import path
from .views import OrderCreateView, OrderUpdateView, OrderListView, OrderDetailView, OrderDeleteView


app_name = 'orders'

urlpatterns = [
    path('', OrderListView.as_view(), name='orders-list'),
    path('<int:pk>/', OrderDetailView.as_view(), name='order-detail'),
    path('create/', OrderCreateView.as_view(), name='order-create'),
    path('<int:pk>/update/', OrderUpdateView.as_view(), name='order-update'),
    path('<int:pk>/delete/', OrderDeleteView.as_view(), name='order-delete'),
]