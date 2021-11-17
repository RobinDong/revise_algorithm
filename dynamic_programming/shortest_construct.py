# Find the shortest sub-string sequence for the target string


def shortest_construct(target_str, array, mem):
    if target_str in mem:
        return mem[target_str]

    if target_str == "":
        return []

    shortest_arr = None
    for item in array:
        if not target_str.startswith(item):
            continue
        remain = target_str[len(item) :]
        result = shortest_construct(remain, array, mem)
        if result is None:
            continue
        result = result + [item]
        if shortest_arr is None or len(shortest_arr) > len(result):
            shortest_arr = result

    mem[target_str] = shortest_arr
    return shortest_arr


if __name__ == "__main__":
    print(shortest_construct("abcdef", ["ab", "abc", "cd", "def", "abcd"], {}))
    print(
        shortest_construct(
            "skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"], {}
        )
    )
    print(shortest_construct("helloworld", ["hello", "world"], {}))
    print(shortest_construct("icestorm", ["storm", "ice", "icest", "or", "m"], {}))
    print(
        shortest_construct(
            "abcdefghijk", ["abcde", "fg", "hij", "k", "bcdef", "ghijk", "a"], {}
        )
    )
    print(
        shortest_construct(
            "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee",
            ["e", "ee"],
            {},
        )
    )
