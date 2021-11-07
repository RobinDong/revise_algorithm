# Get n-th Fibonacci number


def fibonacci(nth, memory):
    if nth in memory:
        return memory[nth]

    if nth <= 1:
        return 1
    else:
        memory[nth] = fibonacci(nth - 1, memory) + fibonacci(nth - 2, memory)
        return memory[nth]


if __name__ == "__main__":
    print(fibonacci(199, {}))
