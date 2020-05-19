#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    division_list = []
    for items in range(list_length):
        product = 0
        try:
            product = my_list_1[items] / my_list_2[items]
        except ZeroDivisionError:
            print("division by 0")
        except TypeError:
            print("wrong type")
        except IndexError:
            print("out of range")
        finally:
            division_list.append(product)
    return division_list
