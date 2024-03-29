#from .models import ()
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from .models import Newsletter_Subscribe
from django.http import JsonResponse
from ipaddr import client_ip
import requests as R


@csrf_exempt
def set_content_index(request):

    # Find request country from ip address
    response = R.get(f'https://freeipapi.com/api/json/{client_ip(request)}')
    data = response.json()
    country = data['countryCode']

    if country == "IR":
        return JsonResponse({'status' : 'fa', 'success' : True})
    elif country in ["SA", "AE", "EG", "IQ", "KW", "SD", "SY", "YE"]: 
        return JsonResponse({'status' : 'ar', 'success' : True})
    else:
        return JsonResponse({'status' : 'en', 'success' : True})

@csrf_exempt
def set_language(request):
    code = request.POST.get('code')
    if code == "en" :
        return JsonResponse({'status' : 'en', 'success' : True})
    elif code == "fa":
        return JsonResponse({'status' : 'fa', 'success' : True})
    elif code == "ar":
        return JsonResponse({'status' : 'ar', 'success' : True})
    else:
        return JsonResponse({'status' : 'BAD_REQUEST_403', 'success' : False})

@csrf_exempt
def add_newsletter_subscribe(request):
    email = request.POST.get('email')
    lang = request.POST.get('lang')
    if email:
        if lang == 'fa':
            if Newsletter_Subscribe.objects.filter(email=email).exists():
                return JsonResponse({'status': 'شما قبلا عضو خبرنامه شده اید', 'success': False})
            else:
                Newsletter_Subscribe.objects.create(
                    lang=lang,
                    email=email,
                )
                return JsonResponse({'status': 'سپاس از عضویت شما', 'success': True})
        elif lang == 'ar':
            if Newsletter_Subscribe.objects.filter(email=email).exists():
                return JsonResponse({'status': 'لقد اشتركتَ في النشرة الإخبارية من قبل.', 'success': False})
            else:
                Newsletter_Subscribe.objects.create(
                    lang=lang,
                    email=email,
                )
                return JsonResponse({'status': 'شكراً لعضويتك.', 'success': True})
        else:
            if Newsletter_Subscribe.objects.filter(email=email).exists():
                return JsonResponse({'status': 'You have previously subscribed to the newsletter.', 'success': False})
            else:
                Newsletter_Subscribe.objects.create(
                    lang=lang,
                    email=email,
                )
                return JsonResponse({'status': 'Thank you for your membership.', 'success': True})
    else:
        if lang == 'fa':
            return JsonResponse({'status': 'لطفا یک رایانامه معتبر وارد کنید', 'success': False})
        elif lang == 'ar':
            return JsonResponse({'status': 'يرجى إدخال بريد إلكتروني صالح', 'success': False})
        else:
            return JsonResponse({'status': 'Please enter a valid email.', 'success': False})