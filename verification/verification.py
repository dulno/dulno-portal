from functools import wraps
from functools import partial
from django.shortcuts import render
from django.http import HttpResponse
from product.dashboard import dashboard
from django.shortcuts import redirect
from django.utils import translation
from django.utils.translation import gettext
from app.settings import RECAPTCHA_TOKEN, GOOGLE_CLIENT_ID

def home_page(function):
  @wraps(function)
  async def home_page(request, *args, **kwargs):
    applyLanguage(request)
    return await function(request, *args, **kwargs)
  return home_page

def applyLanguage(request):
  language = request.COOKIES.get("dulno-home-language")
  if (language is None):
    translation.activate("en")
  translation.activate(language)

@home_page
async def login(request):
  token = request.COOKIES.get('token')
  redirectUrl = request.GET.get('redirect', '')
  if token is None or redirectUrl != '':
    return render(request, 'login.html', {'title': gettext("login.title"),
      'css': ['css/base/home-language.css', 'css/base/2fa.css', 'css/verification/login.css'],
      'redirect': redirectUrl, 'google_client_id': GOOGLE_CLIENT_ID})
  return redirect("/dashboard/")

@home_page
async def signup(request):
  redirect = request.GET.get('redirect', '')
  return render(request, 'signup.html', {'title': gettext("signup.title"),
    'css': ['css/base/home-language.css', 'css/verification/signup.css'],
    'redirect': redirect, 'recaptcha_token': RECAPTCHA_TOKEN})

@home_page
async def signupConfirm(request, member, token):
  redirect = request.GET.get('redirect', '')
  return render(request, 'signup-confirm.html', {'title': gettext("signup.title"),
    'css': ['css/base/home-language.css', 'css/verification/signup-confirm.css'],
    'member': member, 'token': token, 'redirect': redirect})

@home_page
async def loginSignup(request):
  redirect = request.GET.get('redirect', '')
  return render(request, 'login-signup.html', {'title': gettext("login.signup.title"),
    'css': ['css/base/verification-header.css', 'css/base/home-language.css', 'css/verification/login-signup.css'],
    'redirect': redirect})

@home_page
async def payment(request):
  return render(request, 'payment.html', {'title': gettext("payment.title"),
    'css': ['css/base/verification-header.css', 'css/base/home-language.css', 'css/verification/payment.css']})

@home_page
async def paymentComplete(request, token):
  return render(request, 'payment-complete.html', {'title': gettext("payment.complete.title"),
    'css': ['css/base/verification-header.css', 'css/base/home-language.css', 'css/verification/payment-complete.css'],
    'token': token})

@home_page
async def expiration(request):
  return render(request, 'expiration.html', {'title': gettext("expiration.title"),
    'css': ['css/verification/expiration.css', 'css/base/pricing-content.css']})

@home_page
async def sale(request):
  return render(request, 'sale.html', {'title': gettext("sale.title"),
    'css': ['css/verification/sale.css']})

@home_page
async def offer(request, id):
  return render(request, 'offer.html', {'title': gettext("offer.title"),
    'css': ['css/base/verification-header.css', 'css/base/home-language.css', 'css/verification/offer.css'],
    'offer': id})

@home_page
async def passwordResetRequest(request):
  return render(request, 'password-reset-request.html', {'title': gettext("password.reset.request.title"),
    'css': ['css/base/home-language.css', 'css/verification/password-reset-request.css']})

@home_page
async def passwordResetComplete(request, member, token):
  return render(request, 'password-reset-complete.html', {'title': gettext("password.reset.complete.title"),
    'css': ['css/base/home-language.css', 'css/verification/password-reset-complete.css'],
    'member': member, 'token': token})