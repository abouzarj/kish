from django.urls import path
from django.urls.resolvers import URLPattern
from myapp import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('customers/', views.CustomerList.as_view()),
    path('customers/<int:pk>/', views.CustomerDetail.as_view()),
    path('orders/', views.ServiceOrderList.as_view()),
    path('orders/<int:pk>/', views.ServiceOrderDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
