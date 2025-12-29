def sort_string(string: str) -> str:
    return ("").join(sorted(string))


# string.count(char)で置き換え可能
def count_char(string: str, char: str) -> int:
    res = 0
    for s in string:
        if s == char:
            res += 1
    return res


def add_chr_to_set(string: str, set_of_string: set) -> set:
    for char in string:
        set_of_string.add(char)
    return set_of_string


def count_loss(string: str, set_of_compared_string: set) -> int:
    loss = 0
    for char in string:
        if char not in set_of_compared_string:
            loss += 1


def read_file(file_path: str) -> str:
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()


# itertools.groupbyで置き換え可能
def run_length_encoding(string: str) -> list:
    if len(string) == 0:
        return []
    assyuku = []
    focus = string[0]
    current = 1
    for i in range(1, len(string)):
        if string[i] == focus:
            current += 1
        else:
            assyuku.append((focus, current))
            focus = string[i]
            current = 1
    assyuku.append((focus, current))
    return assyuku


def triangle_area(x1, y1, x2, y2, x3, y3):
    return 0.5 * abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))


# math.ceilで置き換え可能
def ceil(target: int, bottom: int) -> int:
    if target % bottom == 0:
        return target // bottom
    else:
        return target // bottom + 1


# math.floorで置き換え可能
def floor(target: int, bottom: int) -> int:
    return target // bottom
