from django.urls import path
from .views import CurrentDateView, IndexView

# creating view for datetime
urlpatterns = [
    path('', IndexView.as_view()),
    path('datetime/', CurrentDateView.as_view()),
]
