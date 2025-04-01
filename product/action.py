from django.shortcuts import render
from django.http import HttpResponse
from base.authentication import authentication_required, isAuthenticated
from django.utils.translation import gettext

@authentication_required
async def actions(request):
  return render(request, 'action/actions.html', {'title': gettext('product.actions.title'),
    'css': ['css/base/product-header.css', 'css/base/product-sidebar.css', 'css/product/action/actions.css']})