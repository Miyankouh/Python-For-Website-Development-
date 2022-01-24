from data import words


def find_common_prefix(words_list):

    s = tuple(zip(*words_list))
    tmp = ''
    for i in s:
        if len(set(i))!=1:
            break
        tmp += i[0]
    return tmp


print(find_common_prefix(words))

