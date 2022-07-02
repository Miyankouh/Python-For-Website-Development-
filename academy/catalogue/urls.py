from django.urls import path
from .views import product_list, product_detail, category_products, product_search, user_profile


urlpatterns = [
    path('product/list', product_list, name='product-list'),
    path('product/search/', product_search, name='product-search'),
    path('product/detail/<int:pk>/', product_detail, name='product-detail'),
    path('category/<int:pk>/products/', category_products, name='product-detail'),
    path('profile/', user_profile, name='user-profile'),
]
