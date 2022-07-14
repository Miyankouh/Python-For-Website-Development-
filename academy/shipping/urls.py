from django.urls import path

from shipping.views import AddressListView, address_create, address_list


urlpatterns = [
    path("list/", AddressListView.as_view(), name="address-list"),
    # path("list/", address_list, name="address-list"),
    path("create/", address_create, name="address-create"),
]
