from django.urls import include, path
from .json import (set_language)


urlpatterns = [
    path('set_language', set_language),
]