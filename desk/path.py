from django.urls import include, path
from .json import (set_content_index, set_language)


urlpatterns = [
    path('set_content_index', set_content_index),
    path('set_language', set_language),
]