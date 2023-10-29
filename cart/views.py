from django.shortcuts import redirect, get_object_or_404
from django.views import generic

from .carts import Cart
from product.models import Product

class AddToCart(generic.View):
    def post(self, *args, **kwargs):
        product = get_object_or_404(Product, id=kwargs.get('product_id'))
        cart = Cart(self.request)
        cart.update(product.id, 1)
        return redirect('product_page', slug=product.slug)
    

class CartItems(generic.TemplateView):
    template_name = 'cart/cart.html'


