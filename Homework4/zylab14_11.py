# Syed Ali
# 1799248

def selection_sort_descend_trace(numbers):
    for i in range(len(numbers) - 1):
        large = i
        for j in range(i + 1, len(numbers)):
            if numbers[large] < numbers[j]:
                large = j
        numbers[i], numbers[large] = numbers[large], numbers[i]
        for value in numbers:
            print(value, end=" ")
        print()
    return numbers


if __name__ == "__main__":
    numbers = []

    numbers = [int(x) for x in input("").split()]
    selection_sort_descend_trace(numbers)
