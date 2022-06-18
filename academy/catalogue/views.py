from django.http import HttpResponse
from catalogue.models import Product


def product_list(request):
    products = Product.objects.all()
    context = "\n".join([f"{product.title}, {product.upc}" for product in products])
    return HttpResponse(context)
