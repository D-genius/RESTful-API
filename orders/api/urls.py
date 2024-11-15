from django.urls import path ,include
from rest_framework import routers
from .. import views

app_name = 'orders'
router = routers.DefaultRouter()
router.register('customers', views.CustomerViewSet)
router.register('orders', views.OrderViewSet)

urlpatterns = [
    path('customers/',
         views.CustomerListView.as_view(),
         name='customer_list'),
    path('customers/<pk>/',
         views.CustomerDetailView.as_view(),
         name='customer_detail'),
    path('orders/',
         views.OrderListView.as_view(),
         name='order_list'),
    path('orders/<pk>',
         views.OrderDetailView.as_view(),
         name='order_detail'),
    path('orders/<pk>/place/',
         views.OrderPlaceView.as_view(),
         name='course_enroll'),
    path('api/', include(router.urls)),
]