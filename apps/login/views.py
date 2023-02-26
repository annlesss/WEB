from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

class log_in(View):
    def get(self, request):
        return render(request, 'auth_shop/index.html')

