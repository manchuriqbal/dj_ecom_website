from django.urls import path
from .views import Checkout, SaveOrder
urlpatterns = [
    path('checkout/', Checkout.as_view(), name="checkout"),
    path('save-order/', SaveOrder.as_view(), name="save_order"),
]