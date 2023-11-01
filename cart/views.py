from django.contrib import messages
from django.shortcuts import redirect, get_object_or_404
from django.views import generic
from django.utils import timezone

from datetime import datetime


from .models import Coupon
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

    def get(self, request, *args, **kwargs):
        product_id = request.GET.get('product_id', None)
        quantity = request.GET.get('quantity', None)
        clear_cart = request.GET.get('clear_cart', False)
        cart = Cart(request)

        if product_id and quantity:
            product = get_object_or_404(Product, id = product_id)
            if int(quantity) > 0:
                if product.in_stock:
                    cart.update(int(product_id), int(quantity))
                    return redirect('cart')
                else:
                    messages.warning(request, 'This product is not in Stock anymore!')
                    return redirect('cart')
            cart.update(int(product_id), int(quantity))
            return redirect('cart')
        
        if clear_cart:
            cart.clear()
            return redirect('cart')
        
        return super().get(request, *args, **kwargs)


class AddCoupon(generic.View):
    def post(self, *args, **kwargs):
        code = self.request.POST.get('code', '')
        coupon = Coupon.objects.filter(code__iexact=code, active=True)

        if coupon.exists():
            coupon = coupon.first()
            expiry_date = coupon.expiry_date
            active_date = coupon.active_date
            minimum_amount = coupon.minimum_amount
            current_date = datetime.date(timezone.now())
            cart = Cart(self.request)

            if current_date > expiry_date:
                messages.warning(self.request, 'Coupon code are Expiry')
                return redirect('cart')
            
            if current_date < active_date:
                messages.warning(self.request, 'Coupon code are Not Start until now')
                return redirect('cart')
            
            if cart.total() < minimum_amount:
                messages.warning(self.request, f'You have to shop minimum ${minimum_amount}. Otherwise you can\'t use this coupon code. ')
                return redirect('cart')

            cart.coupon_add(coupon.id)
            messages.success(self.request, "Coupon code Active Successfully!")
            return redirect('cart')


        else:
            messages.warning(self.request, 'Invalid Coupon Code!')
            return redirect('cart')