from django.urls import path
from .views import RandView

urlpatterns = [
    path('randint/', RandView.as_view()),
]