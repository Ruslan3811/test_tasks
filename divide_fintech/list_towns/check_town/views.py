from django.http import JsonResponse
from .cash import check_in_cash, deleteOldValueInCash, addNewValueInCash
# Create your views here.

db_set = set()

def parse_town(param):
    if (param.find('/') != -1):
        param = param.replace('/', '')
    return param

def check_db(parsed_town):
    if (parsed_town in db_set):
        return True
    db_set.add(parsed_town)
    return False

def findTown(request):
    parsed_town = parse_town(request.GET.get("town"))
    answer = check_in_cash(parsed_town)
    if (answer == False):
        answer = check_db(parsed_town)
    deleteOldValueInCash(parsed_town)
    addNewValueInCash(parsed_town)
    return JsonResponse({parsed_town: answer}, safe=False, json_dumps_params={'ensure_ascii': False})
