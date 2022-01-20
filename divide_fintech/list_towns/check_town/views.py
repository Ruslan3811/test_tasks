
from django.http import JsonResponse
from .models import Town
# Create your views here.
_g_dict_towns = {}

def parse_town(param):
    # town = param.replace("\n", '')
    if (param.find('/') != -1):
        param = param.replace('/', '')
    return param

def check_in_cash(parsed_town):
    answer = _g_dict_towns.get(parsed_town, False)
    if (answer == True):
        del _g_dict_towns[parsed_town]
    elif (len(_g_dict_towns) == 100):
        for key in _g_dict_towns.keys():
            del _g_dict_towns[key]
            break
    _g_dict_towns.setdefault(parsed_town, True)
    return answer

def check_db(parsed_town):
    answer = Town.objects.filter(town=parsed_town).exists()
    if (answer == False):
        Town(town=parsed_town).save()
    return answer

_count = 0

def findTown(request):
    global _count
    parsed_town = parse_town(request.GET.get("town"))
    answer = check_in_cash(parsed_town)
    if (answer == False):
        _count += 1
        answer = check_db(parsed_town)
    return JsonResponse({parsed_town: answer}, safe=False, json_dumps_params={'ensure_ascii': False})
