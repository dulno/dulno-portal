from django.urls import path, include
from . import verification

urlpatterns = [
  path('login/', verification.login),
  path('signup/', verification.signup),
  path('signup/confirm/<str:user>/<str:token>/', verification.signupConfirm),
  path('login-signup/', verification.loginSignup),
  path('payment/', verification.payment),
  path('payment/complete/<str:token>/', verification.paymentComplete),
  path('expiration/', verification.expiration),
  path('offer/<str:id>/', verification.offer),
  path('password/reset/request/', verification.passwordResetRequest),
  path('password/reset/complete/<str:user>/<str:token>/', verification.passwordResetComplete),
]