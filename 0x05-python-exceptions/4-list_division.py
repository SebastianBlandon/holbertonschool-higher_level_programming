#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    list_out = []
    error = 0
    for i in range(list_length):
        try:
            x = (my_list_1[i] / my_list_2[i])
        except IndexError:
            print("out of range")
            error = 1
        except (TypeError or ValueError):
            print("wrong type")
            error = 1
        except ZeroDivisionError:
            print("division by 0")
            error = 1
        finally:
            if error:
                list_out.append(0)
                error = 0
            else:
                list_out.append(x)
    return list_out
