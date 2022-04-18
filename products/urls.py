from django.urls import path
from . import views

app_name = "products"

ProductCreateListViewset = views.ProductCreateListAPI.as_view({
    'get' : 'list',
    'post' : 'create',
})
ProductDetailViewset = views.ProductDetailAPI.as_view({
    'get' : 'retrieve',
    'put' : 'update',
    'delete' : 'destroy',
})
FundingViewset = views.FundingAPI.as_view({
    'get' : 'list',
    'post' : 'create',
})

urlpatterns = [
    path('', ProductCreateListViewset, name='product_list'),
    path('<int:product_id>/', ProductDetailViewset, name='product_detail'),
    path('<int:product_id>/funding/', FundingViewset, name='product_funding'),
]