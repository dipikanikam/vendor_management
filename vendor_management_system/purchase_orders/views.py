from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import PurchaseOrder
from .serializers import PurchaseOrderSerializer
from vendors.jsonhepler import SuccessJson, ErrorJson
from datetime import datetime
from vendors.models import Vendor
from django.db.models import Avg, Count, F, ExpressionWrapper, FloatField

class PurchaseOrderListCreateAPIView(APIView):
    def get(self, request):
        purchase_orders = PurchaseOrder.objects.all()
        serializer = PurchaseOrderSerializer(purchase_orders, many=True)
        if not serializer.data:
            return SuccessJson("No purchase orders found", status.HTTP_200_OK)
        return SuccessJson("All Purchase Orders list", status.HTTP_200_OK, serializer.data)

    def post(self, request):
        request.data['order_date'] = datetime.now()  
        serializer = PurchaseOrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return SuccessJson('Purchase order created successfully', status.HTTP_201_CREATED, serializer.data)
        else:
            return ErrorJson('Invalid data', status.HTTP_400_BAD_REQUEST, serializer.errors)

class PurchaseOrderDetailAPIView(APIView):
    def get_purchase_order(self, po_id):
        try:
            return PurchaseOrder.objects.get(pk=po_id)
        except PurchaseOrder.DoesNotExist:
            return None

    def get(self, request, po_id):
        purchase_order = self.get_purchase_order(po_id)
        if purchase_order:
            serializer = PurchaseOrderSerializer(purchase_order)
            return Response(serializer.data)
        else:
            return ErrorJson('Purchase order not found', status.HTTP_404_NOT_FOUND)

    def put(self, request, po_id):
        purchase_order = self.get_purchase_order(po_id)
        if purchase_order:
            serializer = PurchaseOrderSerializer(purchase_order, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return SuccessJson('Purchase order updated successfully', status.HTTP_200_OK, serializer.data)
            else:
                return ErrorJson('Invalid data', status.HTTP_400_BAD_REQUEST, serializer.errors)
        else:
            return ErrorJson('Purchase order not found', status.HTTP_404_NOT_FOUND)

    def delete(self, request, po_id):
        purchase_order = self.get_purchase_order(po_id)
        if purchase_order:
            purchase_order.delete()
            return SuccessJson('Purchase order deleted successfully', status.HTTP_204_NO_CONTENT)
        else:
            return ErrorJson('Purchase order not found', status.HTTP_404_NOT_FOUND)


class VendorPerformanceAPIView(APIView):
    def get(self, request, vendor_id):
        try:
            vendor = Vendor.objects.get(id=vendor_id)
        except Vendor.DoesNotExist:
            return ErrorJson('Vendor not found', status.HTTP_404_NOT_FOUND)

        # Calculate on-time delivery rate
        completed_orders_count = vendor.purchase_orders.filter(status='completed').count()
        on_time_delivery_count = vendor.purchase_orders.filter(status='completed', delivery_date__lte=F('acknowledgment_date')).count()
        on_time_delivery_rate = (on_time_delivery_count / completed_orders_count) * 100 if completed_orders_count > 0 else 0

        # Calculate quality rating average
        quality_rating_avg = vendor.purchase_orders.filter(status='completed').aggregate(quality_rating_avg=Avg('quality_rating'))['quality_rating_avg'] or 0

        # Calculate average response time
        avg_response_time = vendor.purchase_orders.filter(acknowledgment_date__isnull=False).aggregate(avg_response_time=ExpressionWrapper(Avg(F('acknowledgment_date') - F('issue_date')), output_field=FloatField()))['avg_response_time'] or 0

        # Calculate fulfillment rate
        total_orders_count = vendor.purchase_orders.count()
        fulfilled_orders_count = vendor.purchase_orders.filter(status='completed').count()
        fulfillment_rate = (fulfilled_orders_count / total_orders_count) * 100 if total_orders_count > 0 else 0

        data = {
            'on_time_delivery_rate': on_time_delivery_rate,
            'quality_rating_avg': quality_rating_avg,
            'average_response_time': avg_response_time,
            'fulfillment_rate': fulfillment_rate
        }
        return SuccessJson('Purchase order deleted successfully', status.HTTP_200_OK, data)