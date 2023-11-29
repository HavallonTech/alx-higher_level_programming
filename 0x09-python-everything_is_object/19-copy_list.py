#!/usr/bin/python3
def copy_list(l):
    return (l[:])

if __name__ == "__main__":
    my_list = [1, 2, 3]
    new_list = copy_list(my_list)

    print (new_list)
