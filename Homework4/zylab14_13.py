# Syed Ali
# 1799248

# Global variable
num_calls = 0


def partition(user_ids, i, k):
    pivot_index = (i + k) // 2
    pivot_value = user_ids[pivot_index]

    l = i
    h = k

    while True:
        while user_ids[l] < pivot_value:
            l += 1

        while user_ids[h] > pivot_value:
            h -= 1

        if l >= h:
            return h

        user_ids[l], user_ids[h] = user_ids[h], user_ids[l]

        l += 1
        h -= 1


def quicksort(user_ids, i, k):
    global num_calls
    num_calls += 1

    if i < k:
        partition_index = partition(user_ids, i, k)

        quicksort(user_ids, i, partition_index)
        quicksort(user_ids, partition_index + 1, k)


if __name__ == "__main__":
    user_ids = []
    user_id = input()
    while user_id != "-1":
        user_ids.append(user_id)
        user_id = input()

    # Initial call to quicksort
    quicksort(user_ids, 0, len(user_ids) - 1)

    # Print number of calls to quicksort
    print(num_calls)

    # Print sorted user ids
    for user_id in user_ids:
        print(user_id)
