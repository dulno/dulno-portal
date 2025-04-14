from django.urls import path, include
from . import dashboard, card, stamp, partner, analysis, campaign, package, accessory, help

urlpatterns = [
  path('dashboard/', dashboard.dashboard),
  path('cards/', card.cards),
  path('card/create/', card.createCard),
  path('card/<str:id>/', card.card),
  path('stamps/', stamp.stamps),
  path('stamp/<str:id>/', stamp.stamp),
  path('partner/general/', partner.partnerGeneral),
  path('partner/locations/', partner.partnerLocation),
  path('partner/links/', partner.partnerLink),
  path('analysis/', analysis.analysis),
  path('campaigns/', campaign.campaigns),
  path('campaign/create/', campaign.createCampaign),
  path('campaign/<str:campaign>/notification/<str:notification>/', campaign.campaignNotification),
  path('campaign/<str:id>/', campaign.campaign),
  path('package/general/', package.packageGeneral),
  path('package/payments/', package.packagePayment),
  path('package/upgrade/', package.packageUpgrade),
  path('package/termination/', package.packageTermination),
  path('accessory/purchase/', accessory.accessoryPurchase),
  path('accessory/orders/', accessory.accessoryOrder),
  path('help/', help.help),
]