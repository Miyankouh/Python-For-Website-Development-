from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.http import require_POST
from catalogue.models import Product
from basket.models import Basket

# Create your views here.


@require_POST
def add_to_basket(request):
    # todo-1: check if user basket_id in cookie
    # todo-2: create and assign if doesnt have
    # todo-2-1: Check if user authenticated, set user to the basket
    # todo-3: get product from submitted form
    # todo-4: add product to the user basket
    # todo-5: return to the 'next' url
    # request.cookie.get('basket_id', None):
    
    response = HttpResponseRedirect(request.POST.get('next', '/'))

    basket_id = request.COOKIES.get('basket_id', None)
    if basket_id is None:
        basket = Basket.objects.create()
        response.set_cookie('basket_id', basket.id)
    else:
        try:
            basket = Basket.objects.get(pk=basket_id)
        except Basket.DoesNotExist:
            raise Http404

    if request.user.is_authenticated:
        if basket.user is not None and basket.user != request.user:
            raise Http404
        basket.user = request.user
        basket.save()

    product_id = request.POST.get('product_id', None)
    quantity = request.POST.get('quantity', 1)
    try:
        quantity = int(quantity)
    except:
        quantity = 1

    if product_id is not None:
        try:
            product = Product.objects.get(pk=product_id)
        except Product.DoesNotExist:
            raise Http404
        else:
            basket.add(product, quantity)

    return response
