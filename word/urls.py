from django.urls import path
from .views import word_meaning

urlpatterns = [
    path("word/", word_meaning),
]
