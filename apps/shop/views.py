from django.shortcuts import render
from django.shortcuts import render
from django.views import View

class ViewShop(View):
    def get(self, request):
        return render(request, 'shop/shop.html')

# Create your views here.
class ViewSingleProduct(View):
    def get(self, request):
        return render(request, 'shop/product-single.html')