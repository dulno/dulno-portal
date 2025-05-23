from django.shortcuts import render
from django.http import HttpResponse
from base.authentication import authentication_required, isAuthenticated
from django.utils.translation import gettext

@authentication_required
async def campaigns(request):
  return render(request, 'campaign/campaigns.html', {'title': gettext('product.campaigns.title'),
    'css': ['css/base/product-header.css', 'css/base/product-sidebar.css',
      'css/product/campaign/campaigns.css']})

@authentication_required
async def createCampaign(request):
  return render(request, 'campaign/campaign-create.html', {'title': gettext('product.campaign.create.title'),
    'css': ['css/base/product-header.css', 'css/base/product-sidebar.css',
      'css/product/campaign/campaign-header.css', 'css/product/campaign/campaign-create.css']})

@authentication_required
async def campaignGeneral(request, id):
  return render(request, 'campaign/campaign-general.html', {'title': gettext('product.campaign.general.title'),
    'css': ['css/base/product-header.css', 'css/base/product-sidebar.css',
      'css/product/campaign/campaign-header.css', 'css/product/campaign/campaign-general.css'],
    'id': id})

@authentication_required
async def campaignNotifications(request, id):
  return render(request, 'campaign/campaign-notifications.html', {'title': gettext('product.campaign.notifications.title'),
    'css': ['css/base/product-header.css', 'css/base/product-sidebar.css',
      'css/product/campaign/campaign-header.css', 'css/product/campaign/campaign-notifications.css'],
    'id': id})

@authentication_required
async def campaignNotification(request, campaign, notification):
  return render(request, 'campaign/campaign-notification.html', {'title': gettext('product.campaign.notification.title'),
    'css': ['css/base/product-header.css', 'css/base/product-sidebar.css',
      'css/product/campaign/campaign-header.css', 'css/product/campaign/campaign-notification.css'],
    'campaign': campaign, 'notification': notification})

@authentication_required
async def campaignCoupon(request, id):
  return render(request, 'campaign/campaign-coupon.html', {'title': gettext('product.campaign.coupon.title'),
    'css': ['css/base/product-header.css', 'css/base/product-sidebar.css',
      'css/product/campaign/campaign-header.css', 'css/product/campaign/campaign-coupon.css'],
    'id': id})