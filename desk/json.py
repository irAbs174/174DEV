#from .models import ()
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse


@csrf_exempt
def set_content_index(request):
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