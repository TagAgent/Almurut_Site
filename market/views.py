import datetime

from django.shortcuts import render
from django.views.generic import TemplateView

from market.models import Product


class HomeView(TemplateView):
    template_name = 'index.html'

class ProductListView(TemplateView):
    template_name = 'product-list.html'

    def get_context_data(self, **kwargs):
        products = Product.objects.all()

        context = {
            'products': products,
            'now': datetime.datetime.now().date(),
        }
        return context
