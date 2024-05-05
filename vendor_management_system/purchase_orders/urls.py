from django.urls import path
from .views import PurchaseOrderListCreateAPIView, PurchaseOrderDetailAPIView, VendorPerformanceAPIView

urlpatterns = [
    path('purchase_orders/', PurchaseOrderListCreateAPIView.as_view(), name='purchase-order-list-create'),
    path('purchase_orders/<int:po_id>/', PurchaseOrderDetailAPIView.as_view(), name='purchase-order-detail'),
    path('vendors/<int:vendor_id>/performance/', VendorPerformanceAPIView.as_view(), name='vendor-performance'),

]
