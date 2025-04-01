from django.shortcuts import render
from django.http import HttpResponse
from base.authentication import authentication_required, isAuthenticated
from django.utils.translation import gettext

@authentication_required
async def analysis(request):
  return render(request, 'analysis/analysis.html', {'title': gettext('product.analysis.title'),
    'css': ['css/base/product-header.css', 'css/base/product-sidebar.css', 'css/product/analysis/analysis.css']})