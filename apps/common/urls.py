from django.urls import path
from .views import CurrentDateView, IndexView, Line

# creating view for datetime
urlpatterns = [
    path('', IndexView.as_view()),
    path('datetime/', CurrentDateView.as_view()),
    path('hello/', Line.as_view()),
]
