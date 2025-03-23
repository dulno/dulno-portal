from django.urls import path, include
from . import dashboard, package, help

urlpatterns = [
  path('dashboard/', dashboard.dashboard),
  path('package/general/', package.packageGeneral),
  path('package/limitations/', package.packageLimitation),
  path('package/payments/', package.packagePayment),
  path('package/upgrade/', package.packageUpgrade),
  path('package/termination/', package.packageTermination),
  path('help/', help.help),
]