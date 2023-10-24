#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result_list = []
    for listitem in range(list_length):
        try:
            a = my_list_1[listitem]
            b = my_list_2[listitem]
            if isinstance(a, (int, float)) and isinstance(b, (int, float)):
                temp = a / b
                result_list.append(temp)
            else:
                print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
            result_list.append(0)
        except TypeError:
            print("wrong type")
            result_list.append(0)
        except IndexError:
            print("out of range")
    return (result_list)
