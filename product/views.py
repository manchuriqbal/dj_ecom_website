from typing import Any
from django.views import generic

from .models import Category, Product, Slider


class Home(generic.TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            {
                'featured_category': Category.objects.filter(featured=True),
                'featured_product': Product.objects.filter(featured=True),
                'slider': Slider.objects.filter(show=True),
            }
        )
        return context

class ProductDetails(generic.DetailView):
    model = Product
    template_name = 'product/product-page.html'
    slug_url_kwarg = 'slug'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['related_products'] = self.get_object().related
        return context
    

class CategoryDetails(generic.DetailView):
    model = Category
    template_name = 'product/category-page.html'
    slug_url_kwarg = 'slug'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = self.get_object().products.all
        return context
    


class ProductListView(generic.ListView):
    model = Product
    template_name = "product/product-list.html"
    context_object_name = "object_list"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
