import sys


def fv(names, name):
    start_name, finish_name = separete_names(names)
    letters_with_numbers = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5,'f': 6,'g': 7,'h': 8,'i': 9,'j': 10,'k': 11,'l': 12,'m': 13,'n': 14,
               'o': 15,'p': 16,'q': 17,'r': 18,'s': 19,'t': 20,'u': 21,'v': 22,'w': 23,'x': 24,'y': 25,'z': 26}
    numbers_with_letters = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h', 9: 'i', 10: 'j', 11: 'k',
                            12: 'l', 13: 'm', 14: 'n',
                            15: 'o', 16: 'p', 17: 'q', 18: 'r', 19: 's', 20: 't', 21: 'u', 22: 'v', 23: 'w', 24: 'x',
                            25: 'y', 26: 'z'}
    cur_min_value = sys.maxsize
    count_itterat = 0
    start = ''
    finish = ''
    while cur_min_value > 1 and count_itterat < 100:
        count_itterat += 1
        start, min_value_s = find_min_value(start_name, name[0:int((len(name))/2)], letters_with_numbers)
        finish, min_value_f = find_min_value(finish_name, name[int((len(name)) / 2):len(name)], letters_with_numbers)
        start_name = find_neighbors(start, numbers_with_letters, letters_with_numbers)
        finish_name = find_neighbors(finish, numbers_with_letters, letters_with_numbers)
        if min_value_s + min_value_f < cur_min_value:
            cur_min_value = min_value_s + min_value_f
    return start + finish


def find_neighbors(name, numbers_with_letters, letter_with_numbers):
    new_names = []
    for i in range(len(name)):
        cur_number = letter_with_numbers[name[i:i+1]]
        cur_number_bottom = cur_number - 1
        if cur_number == 1:
            cur_number_bottom = 26
        cur_number_top = cur_number + 1
        if cur_number == 26:
            cur_number_top = 1
        add_in_list(numbers_with_letters, cur_number_bottom, name, new_names, i)
        add_in_list(numbers_with_letters, cur_number_top, name, new_names, i)
    return new_names

def add_in_list(numbers_with_letters, number, name, new_names, i):
    name = name[0:i] + numbers_with_letters[number] + name[i + 1:len(name)]
    new_names.append(name)


def separete_names(names):
    start_name = []
    finish_name = []
    for name in names:
        start_name.append(name[0:int((len(name)) / 2)])
        finish_name.append(name[int((len(name)) / 2):len(name)])
    return  start_name, finish_name

def find_min_value(all_names, name, letters):
    cur_name = all_names[0]
    min_value = sys.maxsize
    for element in all_names:
        cur_value = 0
        for i in range(len(name)):
            cur_value += abs(letters[element[i]] - letters[name[i]])
        if cur_value < min_value:
            min_value = cur_value
            cur_name = element
    return cur_name, min_value
