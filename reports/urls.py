from django.urls import path
from .views import (
    ReportCreateView, ReportUpdateView, ReportListView, ReportDetailView,
    ReportDeleteView, generate_pdf, create
)


app_name = 'reports'

urlpatterns = [
    path('', ReportListView.as_view(), name='reports-list'),
    path('pdf/<int:pk>/', generate_pdf, name='pdf'),
    path('<int:pk>/', ReportDetailView.as_view(), name='report-detail'),
    path('create/', create, name='report-create'),
    path('<int:pk>/update/', ReportUpdateView.as_view(), name='report-update'),
    path('<int:pk>/delete/', ReportDeleteView.as_view(), name='report-delete'),
]