def add_two_numbers() -> int:
    user_input = input()
    user_input_split = user_input.split(",")
    res = 0

    for i in range(2):
        res += int(user_input_split[i])

    return res


# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
