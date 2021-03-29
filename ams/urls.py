from django.urls import path
from .views import AMSCreateView, AMSUpdateView, AMSListView, AMSDetailView, AMSDeleteView


app_name = 'ams'

urlpatterns = [
    path('', AMSListView.as_view(), name='ams-list'),
    path('<int:pk>/', AMSDetailView.as_view(), name='ams-detail'),
    path('create/', AMSCreateView.as_view(), name='ams-create'),
    path('<int:pk>/update/', AMSUpdateView.as_view(), name='ams-update'),
    path('<int:pk>/delete/', AMSDeleteView.as_view(), name='ams-delete'),
]