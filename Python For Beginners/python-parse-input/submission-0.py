from typing import List

def read_integers() -> List[int]:
    line  = input()
    strings  = line .split(",")
    res = [0] * len(strings)

    for i in range(len(strings)):
        res[i] = int(strings[i])

    return res


# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
