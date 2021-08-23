from django.urls import path
from .views import Distance

urlpatterns = [
    path('distance/', Distance.as_view()),
]
