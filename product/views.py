from django.views import generic


class Home(generic.TemplateView):
    template_name = 'home.html'

class ProductDetails(generic.TemplateView):
    template_name = 'product/product-page.html'
