from django.shortcuts import render
from django.http import HttpResponse
from base.authentication import authentication_required, isAuthenticated
from django.utils.translation import gettext

@authentication_required
async def coupons(request):
  return render(request, 'coupon/coupons.html', {'title': gettext('product.coupons.title'),
    'css': ['css/base/product-header.css', 'css/base/product-sidebar.css', 'css/product/coupon/coupons.css']})

@authentication_required
async def coupon(request, id):
  return render(request, 'coupon/coupon.html', {'title': gettext('product.coupon.title'),
    'css': ['css/base/product-header.css', 'css/base/product-sidebar.css', 'css/product/coupon/coupon.css'],
    'id': id})