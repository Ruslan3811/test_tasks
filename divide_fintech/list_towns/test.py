import l as l
import requests

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
            lst.append(line)
    return lst

def createNewFile():
    unsorted_list = []
    for x in range(10):
        unsorted_list += unsortList()
    with open("unsorted_file.txt", "w", encoding="utf-8") as file:
        for town in unsorted_list:
            file.write(town)
    return "unsorted_file.txt", unsorted_list

def get():
    response = requests.get('http://127.0.0.1:8000/check_town/')
    print(response.content)

if __name__=="__main__":
    # file_name, town_list = createNewFile()
    town_list = getListTownsFromFile()
    for town in town_list:
        print(town)

