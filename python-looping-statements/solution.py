def countdown_with_skip(start: int) -> list:
    """
    Using a while loop, count down from `start` to 1 (inclusive),
    appending each number to a list, but skip appending any
    number that is exactly 3 (use continue for this).
    Do not use break here.
    Return the resulting list.
    """
    res = []
    num = start
    while num >= 1:
        if num == 3:
            num -= 1  # Crucial: must decrement before continue to avoid infinite loop
            continue
        res.append(num)
        num -= 1
    return res


def find_first_negative(numbers: list) -> int | None:
    """
    Using a while loop with an index variable, find and return
    the first negative number in `numbers`. Use break once found.
    If no negative number exists, use the loop's else clause to
    return None after the loop completes normally.
    """
    idx = 0
    while(idx < len(numbers)):
        if numbers[idx] < 0:
            break
        idx += 1
    else:
        return None
    return numbers[idx]


def sum_with_index(numbers: list) -> dict:
    """
    Using a for loop with enumerate(), build and return a
    dictionary mapping each index to the running sum of all
    numbers up to and including that index.

    Example: sum_with_index([10, 20, 30])
    -> {0: 10, 1: 30, 2: 60}
    """
    map = {}
    sum = 0
    for idx, val in enumerate(numbers):
        sum += val
        map[idx] = sum
    return map


def manual_iteration_trace(items: list) -> list:
    """
    Without using a for loop, replicate what a for loop does
    internally: use iter() to get an iterator from `items`, then
    repeatedly call next() on it inside a while loop, catching
    StopIteration to know when to stop.

    Return a list of all elements retrieved this way, in order
    (it should exactly match the original `items` list).
    """
    res = []
    list_itr = iter(items)
    while(True):
        try:
            nxt = next(list_itr)
            res.append(nxt)
        except StopIteration:
            break
    return res
