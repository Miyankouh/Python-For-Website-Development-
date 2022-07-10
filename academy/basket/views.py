from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.http import require_POST
from basket.forms import AddToBasketForm
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

    basket = Basket.get_basket(request.COOKIES.get('basket_id', None))
    if basket is None:
        raise Http404

    response.set_cookie('basket_id', basket.id)

    if not basket.validate_user(request.user):
        raise Http404

    form = AddToBasketForm(request.POST)
    if form.is_valid():
        form.save(basket=basket)

    return response
