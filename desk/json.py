#from .models import ()
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse


@csrf_exempt
def set_language(request):
    return JsonResponse({'status' : '=>=>=>=> SUCCESS <=<=<=<=', 'success' : True})