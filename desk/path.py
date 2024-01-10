from django.urls import include, path
from .json import (set_content_index, set_language, add_newsletter_subscribe)


urlpatterns = [
    path('set_content_index', set_content_index),
    path('set_language', set_language),
    path('newsletter', add_newsletter_subscribe)
]