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

class ProductDetails(generic.TemplateView):
    template_name = 'product/product-page.html'
