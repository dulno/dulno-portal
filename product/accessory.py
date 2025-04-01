from django.shortcuts import render
from django.http import HttpResponse
from base.authentication import authentication_required, isAuthenticated
from django.utils.translation import gettext

@authentication_required
async def accessories(request):
  return render(request, 'accessory/accessories.html', {'title': gettext('product.accessories.title'),
    'css': ['css/base/product-header.css', 'css/base/product-sidebar.css', 'css/product/accessory/accessories.css']})