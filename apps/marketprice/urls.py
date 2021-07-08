from django.urls import path
from .views import get_finland_prices, get_estonia_prices

urlpatterns = [
    path('get-finland-prices', get_finland_prices, name='get-finland-prices'),
    path('get-estonia-prices', get_estonia_prices, name='get-estonia-prices'),
]