from django.urls import path
from .views import log_in

urlpatterns = [
    path('login/', log_in.as_view())
]
