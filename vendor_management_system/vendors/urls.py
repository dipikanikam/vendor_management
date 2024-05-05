from django.urls import path
from .views import VendorListCreateAPIView, VendorDetailAPIView

urlpatterns = [
    path('vendors/', VendorListCreateAPIView.as_view(), name='vendor-list-create'),
    path('vendors/<int:vendor_id>/', VendorDetailAPIView.as_view(), name='vendor-detail'),

]