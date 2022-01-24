_g_cash_dict_towns = {}
_g_cash_uniq_towns = set()

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.back = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        if (self.head is None):
            self.head = Node(data)
            self.tail = self.head
            return self.tail
        else:
            new = Node(data)
            new.back = self.tail
            self.tail.next = new
            self.tail = new
            return self.tail

    def deleteLinkNode(self, obj):
        back_obj = obj.back
        next_obj = obj.next
        if (back_obj is None and next_obj is None):
            self.head = None
            self.tail = None
            return
        if (back_obj is None or next_obj is None):
            if (back_obj is None):
                self.head = next_obj
                if (next_obj is not None):
                    self.head.back = None
            if (next_obj is None):
                self.tail = back_obj
                if (back_obj is not None):
                    back_obj.next = None
            return None
        back_obj.next = next_obj
        next_obj.back = back_obj
        del obj
        return None

    def popleft(self):
        if (self.head is not None):
            self.head = self.head.next
            if (self.head is not None):
                self.head.back = None
            else:
                self.tail = None

_g_cash_LinkedLists_towns = DoublyLinkedList()

def check_in_cash(parsed_town):
    return parsed_town in _g_cash_uniq_towns

def deleteOldValueInCash(parsed_town):
    if (parsed_town in _g_cash_uniq_towns):
        obj_town = _g_cash_dict_towns[parsed_town]
        _g_cash_LinkedLists_towns.deleteLinkNode(obj_town)
        del _g_cash_dict_towns[parsed_town]
        _g_cash_uniq_towns.remove(parsed_town)
    elif (len(_g_cash_uniq_towns) == 100 and parsed_town not in _g_cash_uniq_towns):
        town = _g_cash_LinkedLists_towns.head.data
        _g_cash_LinkedLists_towns.popleft()
        del _g_cash_dict_towns[town]
        _g_cash_uniq_towns.remove(town)
    return None

def addNewValueInCash(town):
    obj_town = _g_cash_LinkedLists_towns.append(town)
    _g_cash_uniq_towns.add(town)
    _g_cash_dict_towns[town] = obj_town
    return None

