# Find the count sub-string sequence for the target string


def count_construct(target_str, array, mem):
    if target_str in mem:
        return mem[target_str]

    if target_str == "":
        return 1

    count = 0
    for item in array:
        if not target_str.startswith(item):
            continue
        remain = target_str[len(item) :]
        result = count_construct(remain, array, mem)
        count += result

    mem[target_str] = count
    return count


if __name__ == "__main__":
    print(count_construct("abcdef", ["ab", "abc", "cd", "def", "abcd"], {}))
    print(
        count_construct(
            "skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"], {}
        )
    )
    print(count_construct("helloworld", ["hello", "world"], {}))
    print(count_construct("icestorm", ["storm", "ice", "icest", "or", "m"], {}))
    print(
        count_construct(
            "abcdefghijk", ["abcde", "fg", "hij", "k", "bcdef", "ghijk", "a"], {}
        )
    )
    print(
        count_construct(
            "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee",
            ["e", "ee"],
            {},
        )
    )
