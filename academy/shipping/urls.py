from django.urls import path

from shipping.views import address_create, address_list


urlpatterns = [
    path("list/", address_list, name="address-list"),
    path("create/", address_create, name="address-create"),
]
