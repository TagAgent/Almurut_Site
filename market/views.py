import datetime

from django.http import Http404
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView

from .models import Product, ProductRating
from users.models import CustomUser


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

class ProductDetailView(TemplateView):
    template_name = 'product-detail.html'

    def get_context_data(self, **kwargs):
        try:
            product = Product.objects.get(id=kwargs['pk'])
        except Product.DoesNotExist:
            raise Http404
        # user = self.request.user
        #
        # try:
        #     my_product_rating = ProductRating.objects.get(product=product, user=user)
        #     rating = my_product_rating.rating
        # except ProductRating.DoesNotExist:
        rating = 0

        product_rating_list = ProductRating.objects.filter(product=product)
        total_value = 0
        for product_rating in product_rating_list:
            total_value += product_rating.rating

        average_rating = total_value / (len(product_rating_list) + 1)

        product_category = product.category
        category_other_product_list = (
            Product.objects
            .filter(category=product_category)
            .exclude(id=product.id)
        )

        context = {
            'product': product,
            'rating': rating,
            'average_rating': average_rating,
            'other_products': category_other_product_list,
            'now': datetime.datetime.now().date(),
            'other_products_len': len(category_other_product_list)
        }
        return context

class SendFeedbackView(View):
    """Вью для сохранения отзыва для конкретного товара"""

    def post(self, request, *args, **kwargs):
        data = request.POST
        rating_value = data['rating_value']

        product = Product.objects.get(id=kwargs['pk'])
        user = request.user
        if user.is_authenticated:
            try:
                product_rating = ProductRating.objects.get(product=product, user=user)
            except ProductRating.DoesNotExist:
                # ставим оценку, если не было существующей оценки
                ProductRating.objects.create(
                    rating=rating_value,
                    product=product,
                    user=user,
                    message=data['comment'],
                )
                return redirect('product-detail-url', pk=product.id)

            product_rating.rating = rating_value
            product_rating.save()
            return redirect('product-detail-url', pk=product.id)
        else:
            return redirect('/login/')

class FavoritesView(TemplateView):
    """Вью для избранных товаров"""
    template_name = 'favorites.html'

    def get_context_data(self, **kwargs):
        user = self.request.user

        context = {
            'my_favorite_products': user.favorite_products.all()
        }
        return context


class AddProductToFavoriteView(TemplateView):
    """Вью для добавления товара в избранное"""
    template_name = 'favorites.html'

    def get_context_data(self, **kwargs):
        user = self.request.user

        product_id = kwargs['pk']
        product = Product.objects.get(id=product_id)
        user.favorite_products.add(product)
        user.save()

        context = {
            'my_favorite_products': user.favorite_products.all()
        }
        return context


class DeleteProductFromFavoriteView(TemplateView):
    """Вью для удаления товара в избранное"""
    template_name = 'favorites.html'

    def get_context_data(self, **kwargs):
        user = self.request.user

        product_id = kwargs['pk']
        product = Product.objects.get(id=product_id)
        user.favorite_products.remove(product)
        user.save()

        context = {
            'my_favorite_products': user.favorite_products.all()
        }
        return context
