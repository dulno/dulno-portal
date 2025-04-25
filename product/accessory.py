from django.shortcuts import render
from django.http import HttpResponse
from base.authentication import authentication_required, isAuthenticated
from django.utils.translation import gettext

@authentication_required
async def accessoryPurchase(request):
  return render(request, 'accessory/accessory-purchase.html', {'title': gettext('product.accessory.purchase.title'),
    'css': ['css/base/product-header.css', 'css/base/product-sidebar.css',
      'css/product/accessory/accessory-tab.css', 'css/product/accessory/accessory-purchase.css']})

@authentication_required
async def accessoryOrder(request):
  return render(request, 'accessory/accessory-order.html', {'title': gettext('product.accessory.order.title'),
    'css': ['css/base/product-header.css', 'css/base/product-sidebar.css',
      'css/product/accessory/accessory-tab.css', 'css/product/accessory/accessory-order.css']})