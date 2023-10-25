from django.urls import path
from .views import *

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('product-page', ProductDetails.as_view(), name='product_page'),
]