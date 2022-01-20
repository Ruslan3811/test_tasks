def getListTownsFromFile():
    lst = []
    with open("unsorted_file.txt", "r", encoding="utf-8") as file:
        while True:
            line = file.readline()
            if not line:
                break
            lst.append(line[0:-1])
    return lst

if __name__=="__main__":
    town_list = getListTownsFromFile()
    town_set = set()
    with open("etalon_output.txt", "w", encoding="utf-8") as file:
        for town in town_list:
            if (town in town_set):
                file.write(f'{town} : True\n')
            else:
                town_set.add(town)
                file.write(f'{town} : False\n')

