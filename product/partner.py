from django.shortcuts import render
from django.http import HttpResponse
from base.authentication import authentication_required, isAuthenticated
from django.utils.translation import gettext

@authentication_required
async def partner(request):
  return render(request, 'partner/partner.html', {'title': gettext('product.partner.title'),
    'css': ['css/base/product-header.css', 'css/base/product-sidebar.css', 'css/product/partner/partner.css']})