from django.urls import path
from .views import ViewShop, ViewSingleProduct

app_name = 'shop'
urlpatterns = [
    path('', ViewShop.as_view(), name='shop'),
    path('', ViewSingleProduct.as_view(), name='product'),
]