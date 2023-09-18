from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path
from .api import API_DATA_INDEX

urlpatterns = [
    path('API_DATA/index', API_DATA_INDEX.as_view(), name='INDEXAPI'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]