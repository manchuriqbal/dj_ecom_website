from typing import Any
from django.db.models import Q
from django.http import HttpRequest, HttpResponse
from django.views import generic
from django.shortcuts import render

from .models import Category, Product, Slider

from cart.carts import Cart
from django.core.paginator import (
    Paginator,
    PageNotAnInteger,
    EmptyPage,
    InvalidPage
)


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
    

class CustomPaginator:
    def __init__(self, request,  queryset, paginate_by):
        self.paginator = Paginator(queryset, paginate_by)
        self.queryset = queryset
        self.paginate_py = paginate_by
        self.page = request.GET.get('page', 1)
    
    def get_queryset(self):
        try:
            queryset = self.paginator.page(self.page)
        except PageNotAnInteger:
            queryset = self.paginator.page(1)
        except EmptyPage:
            queryset = self.paginator.page(1)
        except InvalidPage:
            queryset = self.paginator.page(1)

        return queryset
    
        


class ProductListView(generic.ListView):
    model = Product
    template_name = "product/product-list.html"
    context_object_name = "object_list"
    paginate_by = 8

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        page_obj = CustomPaginator(self.request, self.get_queryset(), self.paginate_by)
        queryset = page_obj.get_queryset()
        paginator = page_obj.paginator
        context['object_list'] = queryset
        context['paginator'] = paginator
        return context


class SearchProducts(generic.View):
    def get(self, *args, **kwargs):
        key = self.request.GET.get('key', '')
        products = Product.objects.filter(
            Q(title__icontains=key) |
            Q(category__title__icontains=key)
        )
        context = {
            'products':products,
            'key':key
        }
        return render(self.request, 'product/search-products.html', context)