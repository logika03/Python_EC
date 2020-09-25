from random import randint


def main():
    table = to_make_table(10, 10)
    print_table(table)
    new_table = find_similarity(table)
    print_table(new_table)

def to_make_table(height, width):
    table = []
    for i in range(len(table)):
        table.append([])
        for j in range(len(table[i])):
            table[i].append(randint(0, 1))
    return table


def find_similarity(table):
    users_similarity = []
    for i in range(len(table)):
        users_similarity.append([])
        for j in range(len(table)):
            users_similarity[i].append(-1)
    for i in range(len(users_similarity) - 1):
        for k in range(i+1, len(users_similarity)):
            count_first = 0
            count_second = 0
            total = 0
            for j in range(len(table)):
                if table[i][j] == 1 and table[k][j] == 1:
                    total += 1
                if table[i][j] == 1:
                    count_first += 1
                if table[k][j] == 1:
                    count_second += 1
            users_similarity[i][k] = (count_first + count_second)/total
            users_similarity[k][i] = (count_first + count_second)/total
    return users_similarity


def print_table(table):
     for i in range(len(table)):
        print(table[i])