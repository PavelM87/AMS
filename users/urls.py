from django.urls import path
from .views import UserCreateView, UserUpdateView, UserListView, UserDetailView, UserDeleteView, TeamCreateView


app_name = 'users'

urlpatterns = [
    path('', UserListView.as_view(), name='users-list'),
    path('<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('create/', UserCreateView.as_view(), name='user-create'),
    path('team-create/', TeamCreateView.as_view(), name='team-create'),
    path('<int:pk>/update/', UserUpdateView.as_view(), name='user-update'),
    path('<int:pk>/delete/', UserDeleteView.as_view(), name='user-delete'),
]