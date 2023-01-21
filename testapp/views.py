from django.shortcuts import render


from django.views import View
from random import random
from django.http import HttpResponse



class RandView(View):
    def get(self, request):
        random_number = random()
        return HttpResponse(random_number)



