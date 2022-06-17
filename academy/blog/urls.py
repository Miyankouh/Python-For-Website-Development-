from django.urls import path, re_path, register_converter
from blog.utils import FourDigitYear
from blog.views import category_list, post_detail,  post_list


register_converter(FourDigitYear, 'fourdigit')


urlpatterns = [
    path("list/", post_list),
    path("detail/<int:post_id>/", post_detail ),
    path("detail/<uuid:post_uuid>/", post_detail ),
    path("detail/<slug:post_slug>/", post_detail ),
    re_path(r"detail/(?P<post_slug>)[\w-])+/", post_detail),
    path("categories/test/", category_list),
    path("archive/<fourdigit:year>/", post_list),
    re_path(r"archive/(?P<year>[0-9]{2.4})", post_list),
    path("archive/<int:year>/<int:month>/", post_list),

    re_path(r"archive/(?P<code>[0-9]{4})/", post_list),
    re_path(r"archive/(?P<code>[0-9]{6})/", post_list),
]
