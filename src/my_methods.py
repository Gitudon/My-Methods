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
