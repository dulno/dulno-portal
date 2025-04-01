from django.shortcuts import render
from django.http import HttpResponse
from base.authentication import authentication_required, isAuthenticated
from django.utils.translation import gettext

@authentication_required
async def partnerGeneral(request):
  return render(request, 'partner/partner-general.html', {'title': gettext('product.partner.general.title'),
    'css': ['css/base/product-header.css', 'css/base/product-sidebar.css',
      'css/product/partner/partner-tab.css', 'css/product/partner/partner-general.css']})

@authentication_required
async def partnerLocation(request):
  return render(request, 'partner/partner-location.html', {'title': gettext('product.partner.location.title'),
    'css': ['css/base/product-header.css', 'css/base/product-sidebar.css',
      'css/product/partner/partner-tab.css', 'css/product/partner/partner-location.css']})

@authentication_required
async def partnerLink(request):
  return render(request, 'partner/partner-link.html', {'title': gettext('product.partner.link.title'),
    'css': ['css/base/product-header.css', 'css/base/product-sidebar.css',
      'css/product/partner/partner-tab.css', 'css/product/partner/partner-link.css']})