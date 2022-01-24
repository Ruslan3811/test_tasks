from django.test import TestCase
from list_towns.check_town.cash import (check_in_cash,
                                        addNewValueInCash,
                                        deleteOldValueInCash,
                                        _g_cash_uniq_towns)
from list_towns.check_town.views import check_db

from collections import deque

deque_towns = deque()
set_towns = set()
dict_towns = {}

class CashTestCase(TestCase):

    def test_1DoesTownExist1(self):
        town = "Kazan"
        set_towns.add(town)

        answer = check_in_cash(town)
        if (answer == False):
            answer = check_db(town)
        deleteOldValueInCash(town)
        addNewValueInCash(town)
        self.assertEqual(_g_cash_uniq_towns, set_towns)
        print(f"\nset1: {set_towns}\nset2: {_g_cash_uniq_towns}\n[Kazan]")
        #[Kazan]
        town = "Moscow"
        set_towns.add(town)

        answer = check_in_cash(town)
        if (answer == False):
            answer = check_db(town)
        deleteOldValueInCash(town)
        addNewValueInCash(town)
        self.assertEqual(_g_cash_uniq_towns, set_towns)
        print(f"\nset1: {set_towns}\nset2: {_g_cash_uniq_towns}\n[Kazan, Moscow]")
        # [Kazan, Moscow]

        town = "Piter"
        set_towns.add(town)

        answer = check_in_cash(town)
        if (answer == False):
            answer = check_db(town)
        deleteOldValueInCash(town)
        addNewValueInCash(town)
        self.assertEqual(_g_cash_uniq_towns, set_towns)
        print(f"\nset1: {set_towns}\nset2: {_g_cash_uniq_towns}\n[Kazan, Moscow, Piter]")
        # [Kazan, Moscow, Piter]

        town = "Kazan"
        set_towns.add(town)

        answer = check_in_cash(town)
        if (answer == False):
            answer = check_db(town)
        deleteOldValueInCash(town)
        addNewValueInCash(town)
        self.assertEqual(_g_cash_uniq_towns, set_towns)
        print(f"\nset1: {set_towns}\nset2: {_g_cash_uniq_towns}\n[Moscow, Piter, Kazan]")
        # [Moscow, Piter, Kazan]

        town = "Buxton"
        set_towns.add(town)
        set_towns.remove("Moscow")
        answer = check_in_cash(town)
        if (answer == False):
            answer = check_db(town)
        deleteOldValueInCash(town)
        addNewValueInCash(town)
        self.assertEqual(_g_cash_uniq_towns, set_towns)
        print(f"\nset1: {set_towns}\nset2: {_g_cash_uniq_towns}\n[Piter, Kazan, Buxton]")
        # [Piter, Kazan, Buxton]

        town = "Piter"
        set_towns.add(town)
        # set_towns.remove("Moscow")
        answer = check_in_cash(town)
        if (answer == False):
            answer = check_db(town)
        deleteOldValueInCash(town)
        addNewValueInCash(town)
        self.assertEqual(_g_cash_uniq_towns, set_towns)
        print(f"\nset1: {set_towns}\nset2: {_g_cash_uniq_towns}\n[Kazan, Buxton, Piter]")
        # [Kazan, Buxton, Piter]

        town = "Almet"
        set_towns.add(town)
        set_towns.remove("Kazan")
        answer = check_in_cash(town)
        if (answer == False):
            answer = check_db(town)
        deleteOldValueInCash(town)
        addNewValueInCash(town)
        self.assertEqual(_g_cash_uniq_towns, set_towns)
        # [Buxton, Piter, Almet]
        print(f"\nset1: {set_towns}\nset2: {_g_cash_uniq_towns}\n[Buxton, Piter, Almet]")

        town = "Piter"
        set_towns.add(town)
        # set_towns.remove("Buxton")
        answer = check_in_cash(town)
        if (answer == False):
            answer = check_db(town)
        deleteOldValueInCash(town)
        addNewValueInCash(town)
        self.assertEqual(_g_cash_uniq_towns, set_towns)
        # [Buxton, Almet, Piter]
        print(f"\nset1: {set_towns}\nset2: {_g_cash_uniq_towns}\n[Buxton, Almet, Piter]")

        town = "LA"
        set_towns.add(town)
        set_towns.remove("Buxton")
        answer = check_in_cash(town)
        if (answer == False):
            answer = check_db(town)
        deleteOldValueInCash(town)
        addNewValueInCash(town)
        self.assertEqual(_g_cash_uniq_towns, set_towns)
        # [Almet, Piter, LA]
        print(f"\nset1: {set_towns}\nset2: {_g_cash_uniq_towns}\n[Almet, Piter, LA]")

        town = "Buxton"
        set_towns.add(town)
        set_towns.remove("Almet")
        answer = check_in_cash(town)
        if (answer == False):
            answer = check_db(town)
        deleteOldValueInCash(town)
        addNewValueInCash(town)
        self.assertEqual(_g_cash_uniq_towns, set_towns)
        # [Piter, LA, Buxton]
        print(f"\nset1: {set_towns}\nset2: {_g_cash_uniq_towns}\n[Piter, LA, Buxton]]")

        town = "New-York"
        set_towns.add(town)
        set_towns.remove("Piter")
        answer = check_in_cash(town)
        if (answer == False):
            answer = check_db(town)
        deleteOldValueInCash(town)
        addNewValueInCash(town)
        self.assertEqual(_g_cash_uniq_towns, set_towns)
        # [LA, Buxton, New-York]
        print(f"\nset1: {set_towns}\nset2: {_g_cash_uniq_towns}\n [LA, Buxton, New-York]")
    #
    #
    #
    # def test_1DoesTownExist2(self):
    #     town = "Moscow"
    #     dict_towns[town] = 1
    #     set_towns.add(town)
    #     deque_towns.appendleft(town)
    #     answer = check_in_cash("Moscow")
    #     if (answer == False):
    #         check_db(town)
    #         deleteOldValueInCash()
    #     addNewValueInCash(town)
    #     self.assertEqual(False, answer)
    #     print(f"\ndeque1: {deque_towns}\ndeque2: {_g_cash_deque_towns}")
    #     self.assertEqual(deque_towns, _g_cash_deque_towns)
    #     print(f"\n\nset1: {set_towns}\nset2: {_g_cash_uniq_towns}")
    #     self.assertEqual(set_towns, _g_cash_uniq_towns)
    #     print(f"\n\ndict1: {dict_towns}\ndict2: {_g_cash_counting_towns}")
    #     self.assertEqual(dict_towns, _g_cash_counting_towns)
    #
    #
    # def test_1DoesTownExist3(self):
    #     town = "Kazan"
    #     dict_towns[town] = 2
    #     set_towns.add(town)
    #     deque_towns.appendleft(town)
    #     answer = check_in_cash(town)
    #     if (answer == False):
    #         check_db(town)
    #         deleteOldValueInCash()
    #     addNewValueInCash(town)
    #     self.assertEqual(True, answer)
    #     print(f"\ndeque1: {deque_towns}\ndeque2: {_g_cash_deque_towns}")
    #     self.assertEqual(deque_towns, _g_cash_deque_towns)
    #     print(f"\n\nset1: {set_towns}\nset2: {_g_cash_uniq_towns}")
    #     self.assertEqual(set_towns, _g_cash_uniq_towns)
    #     print(f"\n\ndict1: {dict_towns}\ndict2: {_g_cash_counting_towns}")
    #     self.assertEqual(dict_towns, _g_cash_counting_towns)
    #
    # def test_1DoesTownExist4(self):
    #     town = "Buxton"
    #     dict_towns[town] = 1
    #     set_towns.add(town)
    #     deque_towns.appendleft(town)
    #     answer = check_in_cash(town)
    #     if (answer == False):
    #         check_db(town)
    #         deleteOldValueInCash()
    #     addNewValueInCash(town)
    #     self.assertEqual(False, answer)
    #     print(f"\ndeque1: {deque_towns}\ndeque2: {_g_cash_deque_towns}")
    #     self.assertEqual(deque_towns, _g_cash_deque_towns)
    #     print(f"\n\nset1: {set_towns}\nset2: {_g_cash_uniq_towns}")
    #     self.assertEqual(set_towns, _g_cash_uniq_towns)
    #     print(f"\n\ndict1: {dict_towns}\ndict2: {_g_cash_counting_towns}")
    #     self.assertEqual(dict_towns, _g_cash_counting_towns)
    #
    # def test_1DoesTownExist5(self):
    #     town = "Flagstaff"
    #     dict_towns[town] = 1
    #     set_towns.add(town)
    #     set_towns.remove()
    #     deque_towns.appendleft(town)
    #     answer = check_in_cash(town)
    #     if (answer == False):
    #         check_db(town)
    #         deleteOldValueInCash()
    #     addNewValueInCash(town)
    #     self.assertEqual(False, answer)
    #     print(f"\ndeque1: {deque_towns}\ndeque2: {_g_cash_deque_towns}")
    #     self.assertEqual(deque_towns, _g_cash_deque_towns)
    #     print(f"\n\nset1: {set_towns}\nset2: {_g_cash_uniq_towns}")
    #     self.assertEqual(set_towns, _g_cash_uniq_towns)
    #     print(f"\n\ndict1: {dict_towns}\ndict2: {_g_cash_counting_towns}")
    #     self.assertEqual(dict_towns, _g_cash_counting_towns)