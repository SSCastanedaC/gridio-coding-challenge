from django.http import response
from django.test import TestCase, Client

# Create your tests here.

"""
Run test using:
python manage.py test apps.marketprice.tests
"""

class Test(TestCase):
    def test_finland_prices(self):
        client = Client()
        response = client.get('/marketprice/get-finland-prices')
        assert response.status_code == 200
    def test_estonia_prices(self):
        client = Client()
        response = client.get('/marketprice/get-estonia-prices')
        assert response.status_code == 200