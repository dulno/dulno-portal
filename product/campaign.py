from django.shortcuts import render
from django.http import HttpResponse
from base.authentication import authentication_required, isAuthenticated
from django.utils.translation import gettext

@authentication_required
async def campaigns(request):
  return render(request, 'campaign/campaigns.html', {'title': gettext('product.campaigns.title'),
    'css': ['css/base/product-header.css', 'css/base/product-sidebar.css', 'css/product/campaign/campaigns.css']})

@authentication_required
async def createCampaign(request):
  return render(request, 'campaign/campaign-create.html', {'title': gettext('product.campaign.create.title'),
    'css': ['css/base/product-header.css', 'css/base/product-sidebar.css', 'css/product/campaign/campaign-create.css']})

@authentication_required
async def campaign(request, id):
  return render(request, 'campaign/campaign.html', {'title': gettext('product.campaign.title'),
    'css': ['css/base/product-header.css', 'css/base/product-sidebar.css', 'css/product/campaign/campaign.css'],
    'id': id})

@authentication_required
async def campaignNotification(request, id):
  return render(request, 'campaign/campaign-notification.html', {'title': gettext('product.campaign.notification.title'),
    'css': ['css/base/product-header.css', 'css/base/product-sidebar.css', 'css/product/campaign/campaign-notification.css'],
    'id': id})