from django.shortcuts import render
from .models import FinlandMarketPrice, EstoniaMarketPrice
import requests
import json
from datetime import date, datetime, timedelta


# Create your views here.

#Access through /marketprice/get-finland-prices
def get_finland_prices(request):
    """
    Instead of using BS4 to scrapping, I found out that table data
    comes from an API, so I've decided to use requests library to access
    to data directly to improve performance
    """
    url_prices = 'https://www.nordpoolgroup.com/api/marketdata/page/35'
    prices_request = requests.get(url_prices)
    prices = json.loads(prices_request.content)
    prices = prices['data']['Rows']
    finland_prices = []
    for price in prices:
        new_price = FinlandMarketPrice()
        new_price.date = price['StartTime'].split('T')[0]
        new_price.time = price['Name'][0:2]
        new_price.price = float(price['Columns'][0]['Value'].replace(',','.'))
        if new_price.time.isnumeric():
            finland_prices.append(new_price)
    FinlandMarketPrice.objects.all().delete()
    FinlandMarketPrice.objects.bulk_create(finland_prices)
    prices = FinlandMarketPrice.objects.all()
    context = {
        "country_code": "FI",
        "country_name": "Finland",
        "prices": prices
    }
    return render(request, "web/prices.html", context)

#Access through /marketprice/get-finland-prices
def get_estonia_prices(request):
    start_date = date.today() + timedelta(days=1)
    end_date = date.today() + timedelta(days=2)
    url_prices = 'https://dashboard.elering.ee/api/nps/price?start=' + str(start_date) + 'T00%3A00%3A00.000Z' + '&end=' + str(end_date) + 'T00%3A00%3A00.000Z'
    prices_request = requests.get(url_prices)
    prices = json.loads(prices_request.content)
    prices = prices['data']['ee']
    estonia_prices = []
    for price in prices:
        date_time = datetime.fromtimestamp(price['timestamp'])
        new_price = EstoniaMarketPrice()
        new_price.date = date_time
        new_price.time = date_time.hour
        new_price.price = price['price']
        estonia_prices.append(new_price)
    EstoniaMarketPrice.objects.all().delete()
    EstoniaMarketPrice.objects.bulk_create(estonia_prices)
    prices = EstoniaMarketPrice.objects.all()
    context = {
        "country_code": "EE",
        "country_name": "Estonia",
        "prices": prices
    }
    
    return render(request, "web/prices.html", context)