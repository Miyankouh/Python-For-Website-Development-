from django.views.decorators.http import require_http_methods, require_GET, require_POST
from django.contrib.auth.decorators import login_required, user_passes_test, permission_required
from django.db.models import Q
from django.http import HttpResponse
from catalogue.models import Brand, Category, Product, ProductType
from catalogue.utils import check_is_active, check_is_staff

def product_list(request):
    # products = Product.objects.filter(is_active=True)
    # products = Product.objects.exclude(is_active=False)

    # category = Category.objects.first()
    # category = Category.objects.last()

    # category = Category.objects.get(id=1)
    # products = Product.objects.filter(is_active=True, category=category)
    # category = Category.objects.filter(name="Book").first()

    # products = Product.objects.filter(is_active=True, category__name="Book")

    # brand = Brand.objects.filter()
    # product_type = ProductType.objects.filter(title="Book")

    # new_product = Product.objects.create(
    #     product_type = product_type, upc=789465, title="test Product",
    #     description='', category=category, brand=brand
    # )

    products = Product.objects.select_related('category').all()
    context = "\n".join(
        [f"{product.title}, {product.upc}, {product.category.name}" for product in products])
    return HttpResponse(context)


def product_detail(request, pk):
    # try:
    #     product = Product.objects.get(pk=pk)
    # except Product.DoesNotExist:
    #     try:
    #         product = Product.objects.get(pk=pk)
    #     except Product.DoesNotExist:
    #         return HttpResponse("PRODUCT DOES NOT EXIST")

    queryset = Product.objects.filter(
        is_active=True).filter(Q(pk=pk) | Q(upc=pk))
    if queryset.exists():
        product = queryset.first()
        return HttpResponse(f"title: {product.title}")
    return HttpResponse("PRODUCT DOES NOT EXIST")


def category_products(request, pk):
    try:
        category = Category.objects.prefetch_related('products').get(pk=pk)
    except Category.DoesNotExist:
        return HttpResponse('Category does not exist')
    products = category.products.all()

    # products = Product.objects.filter(category=category)

    context = "\n".join(
        [f"{product.title}, {product.upc}" for product in products])
    return HttpResponse(context)


def product_search(request):
    title = request.GET.get('q')

    products = Product.objects.actives(
        title__icontains=title, 
        category__name__icontains=title,
    )
    # products = Product.objects.filter(is_active=True).filter(title__icontains=title).filter(
    #     category__name__icontains=title).filter(category__is_active=True).distinct()
    context = "\n".join(
        [f"{product.title}, {product.upc}" for product in products])
    return HttpResponse(f"search page :\n{context}")


@login_required()
@require_http_methods(request_method_list=['GET'])
@user_passes_test(check_is_active)
@user_passes_test(lambda u: u.is_staff)
@permission_required('transaction.has_score_permission', raise_exception=True)
def user_profile(request):
        return HttpResponse(f"Hello {request.user.username}")


@login_required
# @require_GET
@require_POST
@user_passes_test(lambda u: u.age > 14)
def campaign(request):
    pass
