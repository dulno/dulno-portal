from django.urls import path, include
from . import dashboard, card, stamp, partner, analysis, action, package, accessory, help

urlpatterns = [
  path('dashboard/', dashboard.dashboard),
  path('cards/', card.cards),
  path('stamps/', stamp.stamps),
  path('partner/', partner.partner),
  path('analysis/', analysis.analysis),
  path('actions/', action.actions),
  path('package/general/', package.packageGeneral),
  path('package/payments/', package.packagePayment),
  path('package/upgrade/', package.packageUpgrade),
  path('package/termination/', package.packageTermination),
  path('accessories/', accessory.accessories),
  path('help/', help.help),
]