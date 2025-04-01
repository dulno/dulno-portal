from django.shortcuts import render
from django.http import HttpResponse
from base.authentication import authentication_required, isAuthenticated
from django.utils.translation import gettext

@authentication_required
async def cards(request):
  return render(request, 'card/cards.html', {'title': gettext('product.cards.title'),
    'css': ['css/base/product-header.css', 'css/base/product-sidebar.css', 'css/product/card/cards.css']})

@authentication_required
async def createCard(request):
  return render(request, 'card/card-create.html', {'title': gettext('product.card.create.title'),
    'css': ['css/base/product-header.css', 'css/base/product-sidebar.css', 'css/product/card/card-create.css']})

@authentication_required
async def card(request, id):
  return render(request, 'card/card.html', {'title': gettext('product.card.title'),
    'css': ['css/base/product-header.css', 'css/base/product-sidebar.css', 'css/product/card/card.css'],
    'id': id})