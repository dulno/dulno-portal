from django.shortcuts import render
from django.http import HttpResponse
from base.authentication import authentication_required, isAuthenticated
from django.utils.translation import gettext

@authentication_required
async def balances(request):
  return render(request, 'balance/balances.html', {'title': gettext('product.balances.title'),
    'css': ['css/base/product-header.css', 'css/base/product-sidebar.css', 'css/product/balance/balances.css']})