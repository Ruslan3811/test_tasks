import requests
from time import sleep

def unsortList():
    ret = set()
    with open("towns.txt", "r", encoding="utf-8") as file:
        while True:
            line = file.readline()
            if not line:
                break
            ret.add(line)
    return list(ret)

def getListTownsFromFile():
    lst = []
    with open("unsorted_file.txt", "r", encoding="utf-8") as file:
        while True:
            line = file.readline()
            if not line:
                break
            lst.append(line[0:-1])
    return lst

def createNewFile():
    unsorted_list = []
    for x in range(100):
        unsorted_list += unsortList()
    with open("unsorted_file.txt", "w", encoding="utf-8") as file:
        for town in unsorted_list:
            file.write(town)
    return "unsorted_file.txt", unsorted_list

def get(town):
    response = requests.get('http://127.0.0.1:8000/check_town?town=' + town + '/')
    return response

if __name__=="__main__":
    # file_name, town_list = createNewFile()
    town_list = getListTownsFromFile()
    ind = 0
    k = 0
    with open("output.txt", "w", encoding="utf-8") as file:
        for town in town_list:

            answer = get(town)
            ind += 1
            for key, value in answer.json().items():
                k += 1
                file.write(f'{key} : {value}\n')
            if (ind % 10000 == 0):
                sleep(30)