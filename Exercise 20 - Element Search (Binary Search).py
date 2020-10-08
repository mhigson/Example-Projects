import random
import time

# This code searches a list using (1) regular search and (2) binary search.
# Binary search is helpful when searching for an element in a large data set,
# as the code halves the search range with each pass.
# This claim is substantiated by the run timer for each search method,
# which consistently shows binary search runs faster.

database = sorted(random.sample(range(10000000), 10000000))


def brute_force():
    if user_input in database:
        print(str(user_input) + " is in the list.")
    else:
        print(str(user_input) + " is not in the list.")


def binary_search(_list, _element):
    minimum = 0
    maximum = int(len(_list) - 1)
    while minimum <= maximum:
        mid = int((maximum + minimum) // 2)
        if _list[mid] == _element:
            print(str(_element) + " is in the list.")
            return True
        elif _list[mid] > _element:
            maximum = mid - 1
        elif _list[mid] < _element:
            minimum = mid + 1
    else:
        print(str(_element) + " is not in the list.")
        return False


def search():
    global user_input
    user_input = int(input("Enter a number: "))
    if search_type == 1:
        print()
        start_time = round(float(time.perf_counter()), 4)
        brute_force()
        end_time = round(float(time.perf_counter()), 4)
        print(str(round(end_time - start_time, 4)) + " seconds")
    elif search_type == 2:
        print()
        start_time = round(float(time.perf_counter()), 4)
        binary_search(database, user_input)
        end_time = round(float(time.perf_counter()), 4)
        print(str(round(end_time - start_time, 4)) + " seconds")
    elif search_type == 3:
        print()
        start_time = round(float(time.perf_counter()), 4)
        brute_force()
        end_time = round(float(time.perf_counter()), 4)
        print("Brute Force: " + str(round(end_time - start_time, 4)) + " seconds")
        print()
        start_time = round(float(time.perf_counter()), 4)
        binary_search(database, user_input)
        end_time = round(float(time.perf_counter()), 4)
        print("Binary Search: " + str(round(end_time - start_time, 4)) + " seconds")


def valid_input():
    global search_type
    search_type = int(input("Enter 1 for brute force search, 2 for binary search, or 3 for both: "))
    if int(search_type) in (1, 2, 3):
        search()
    else:
        valid_input()


valid_input()
