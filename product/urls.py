from django.urls import path
from .views import *

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('product-page/<str:slug>/', ProductDetails.as_view(), name='product_page'),
    path('category-page/<str:slug>/', CategoryDetails.as_view(), name='category_page'),
    path('prodcut-list/', ProductListView.as_view(), name='product_list'),
]