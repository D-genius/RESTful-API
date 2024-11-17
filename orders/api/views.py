from rest_framework import generics, viewsets
from django.shortcuts import get_object_or_404
# from django.utils.cache import cache
from rest_framework.views import APIView
from rest_framework.response import Response
from ..models import Customer, Order
from .serializers import CustomerSerializer ,OrderSerializer
import  africastalking
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

africastalking.initialize(username='sandbox', api_key='atsk_207482f1b5057e02a26648d4749e4d7bbdad7d1a99e23896daf5ab4c6559780a3958e716')
sms = africastalking.SMS

def send_sms_alert(customer_name, message):
    recipients = [Customer.phone]
    sms.send(message, recipients)

class CustomerListView(generics.ListAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CustomerDetailView(generics.RetrieveAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    
class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class OrderListView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderDetailView(generics.RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    
    def perform_create(self, serializer):
       order = serializer.save()
       customer_name = Customer.name
       message = f"Hi {customer_name}, your order for {order.item} has been placed."
       send_sms_alert(customer_name, message)
    
    def list(self, request, *args, **kwargs):
        start_date = request.query_params.get('start_date')
        end_date = request.query_params.get('end_date')
        
        if start_date and end_date:
            queryset = self.queryset.filter(time__range=[start_date, end_date])
        else:
            queryset = self.queryset
        return Response(OrderSerializer(queryset, many=True).data)

class OrderPlaceView(APIView):
    def post(self, request, pk, format=None):
        order = get_object_or_404(Order, pk=pk)
        order.customers.add(request.user)
        return Response({'ordered': True})
    
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)
    