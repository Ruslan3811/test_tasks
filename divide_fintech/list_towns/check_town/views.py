
from django.http import JsonResponse

# Create your views here.

_g_list_towns = []

def parse_town(param):
    town = param.replace("\n", '')
    if (param.find('/') != -1):
        town = town.replace('/', '')
    return town


def findTown(request):
    global _g_list_towns
    bool_answer = False
    town = parse_town(request.GET.get("town"))


    data = {town: True}
    return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})
