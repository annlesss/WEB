from django.urls import path
from .views import log_in

urlpatterns = [
    path('auth_shop/', log_in.as_view())
]
