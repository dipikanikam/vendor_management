from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Vendor
from .serializers import VendorSerializer
from .jsonhepler import SuccessJson, ErrorJson

class APIWorking(APIView):
    def get(self, request):
        return Response("APIs are working")

class VendorListCreateAPIView(APIView):
    def get(self, request):
        vendors = Vendor.objects.all()
        serializer = VendorSerializer(vendors, many=True)
        if not serializer.data:
           return SuccessJson("No vendors found", status.HTTP_200_OK)
        return SuccessJson("All Vendors list", status.HTTP_200_OK, serializer.data)

    def post(self, request):
        serializer = VendorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return SuccessJson('Vendor created successfully', status.HTTP_201_CREATED, serializer.data)
        else:
            return ErrorJson('Invalid data', status.HTTP_400_BAD_REQUEST, serializer.errors)

class VendorDetailAPIView(APIView):
    def get_vendor(self, vendor_id):
        try:
            return Vendor.objects.get(pk=vendor_id)
        except Vendor.DoesNotExist:
            return None

    def get(self, request, vendor_id):
        vendor = self.get_vendor(vendor_id)
        if vendor:
            serializer = VendorSerializer(vendor)
            return Response(serializer.data)
        else:
            return ErrorJson('Vendor not found', status.HTTP_404_NOT_FOUND)

    def put(self, request, vendor_id):
        vendor = self.get_vendor(vendor_id)
        if vendor:
            serializer = VendorSerializer(vendor, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return SuccessJson('Vendor updated successfully', status.HTTP_200_OK, serializer.data)
            else:
                return ErrorJson('Invalid data', status.HTTP_400_BAD_REQUEST, serializer.errors)
        else:
            return ErrorJson('Vendor not found', status.HTTP_404_NOT_FOUND)

    def delete(self, request, vendor_id):
        vendor = self.get_vendor(vendor_id)
        if vendor:
            vendor.delete()
            return SuccessJson('Vendor deleted successfully', status.HTTP_204_NO_CONTENT)
        else:
            return ErrorJson('Vendor not found', status.HTTP_404_NOT_FOUND)
