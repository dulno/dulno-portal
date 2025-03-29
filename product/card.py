from django.shortcuts import render
from django.http import HttpResponse
from base.authentication import authentication_required, isAuthenticated
from django.utils.translation import gettext

@authentication_required
async def cards(request):
  return render(request, 'card/cards.html', {'title': gettext('product.cards.title'),
    'css': ['css/base/product-header.css', 'css/base/product-sidebar.css', 'css/product/card/cards.css']})