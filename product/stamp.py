from django.shortcuts import render
from django.http import HttpResponse
from base.authentication import authentication_required, isAuthenticated
from django.utils.translation import gettext

@authentication_required
async def stamps(request):
  return render(request, 'stamp/stamps.html', {'title': gettext('product.stamps.title'),
    'css': ['css/base/product-header.css', 'css/base/product-sidebar.css', 'css/product/stamp/stamps.css']})

@authentication_required
async def stamp(request, id):
  return render(request, 'stamp/stamp.html', {'title': gettext('product.stamp.title'),
    'css': ['css/base/product-header.css', 'css/base/product-sidebar.css', 'css/product/stamp/stamp.css'],
    'id': id})