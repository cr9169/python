def groups(function, my_list):
    i = 1
    key = function(my_list[0])
    values_list = [my_list[0]]
    dictionary = {key: values_list}
    while i < len(my_list):
        key = function(my_list[i])
        values_list = my_list[i]
        if key in dictionary:
            dictionary[key].append(my_list[i])
        else:
            dictionary[key] = [values_list]
        i += 1
    return dictionary


def mod_three(num):
    return num % 3


def main():
    my_list = [1, 3, 4, 5, 7, 9]
    print(groups(mod_three, my_list))


if __name__ == "__main__":
    main()
