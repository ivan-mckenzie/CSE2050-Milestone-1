def recursive_total_price(products):
    """Returns the total of all product prices using recursion"""
    if len(products) == 0:
        return 0.0
    return products[0].get_price() + recursive_total_price(products[1:])


def fewest_coins(coins, amount, memo=None):
    """Returns the fewest coins needed to make amount, or -1 if it can't be made"""
    if memo is None:
        memo = {}
    if amount == 0:
        return 0
    if amount < 0:
        return -1
    if amount in memo:
        return memo[amount]

    best = -1
    for coin in coins:
        result = fewest_coins(coins, amount - coin, memo)
        if result != -1 and (best == -1 or result + 1 < best):
            best = result + 1

    memo[amount] = best
    return best


def bubble_sort(products):
    """Sorts products in place by product id using bubble sort"""
    n = len(products)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if products[j].get_id() > products[j + 1].get_id():
                products[j], products[j + 1] = products[j + 1], products[j]


def selection_sort(products):
    """Sorts products in place by product id using selection sort"""
    n = len(products)
    for i in range(n - 1):
        smallest = i
        for j in range(i + 1, n):
            if products[j].get_id() < products[smallest].get_id():
                smallest = j
        products[i], products[smallest] = products[smallest], products[i]


def insertion_sort(products):
    """Sorts products in place by product id using insertion sort"""
    for i in range(1, len(products)):
        current = products[i]
        j = i - 1
        while j >= 0 and products[j].get_id() > current.get_id():
            products[j + 1] = products[j]
            j -= 1
        products[j + 1] = current


def binary_search(products, product_id):
    """Returns the index of product_id in a sorted product list, or -1 if not found"""
    low = 0
    high = len(products) - 1
    while low <= high:
        mid = (low + high) // 2
        mid_id = products[mid].get_id()
        if mid_id == product_id:
            return mid
        elif mid_id < product_id:
            low = mid + 1
        else:
            high = mid - 1
    return -1



def merge_sort(products):
    """Sorts products in place by product id using merge sort"""
    if len(products) <= 1:
        return

    mid = len(products) // 2
    left = products[:mid]
    right = products[mid:]

    merge_sort(left)
    merge_sort(right)

    i = 0
    j = 0
    k = 0
    while i < len(left) and j < len(right):
        if left[i].get_id() <= right[j].get_id():
            products[k] = left[i]
            i += 1
        else:
            products[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        products[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        products[k] = right[j]
        j += 1
        k += 1


def quick_sort(products):
    """Sorts products in place by product id using quick sort"""
    if len(products) <= 1:
        return

    pivot = products[len(products) - 1]
    smaller = []
    larger = []
    for i in range(len(products) - 1):
        if products[i].get_id() <= pivot.get_id():
            smaller.append(products[i])
        else:
            larger.append(products[i])

    quick_sort(smaller)
    quick_sort(larger)

    combined = smaller + [pivot] + larger
    for i in range(len(products)):
        products[i] = combined[i]


def quick_select(products, k):
    """Returns the product at rank k by product id, where k = 0 is the smallest"""
    if k < 0 or k >= len(products):
        return None

    pivot = products[0]
    smaller = []
    larger = []
    for i in range(1, len(products)):
        if products[i].get_id() < pivot.get_id():
            smaller.append(products[i])
        else:
            larger.append(products[i])

    if len(smaller) == k:
        return pivot
    if len(smaller) > k:
        return quick_select(smaller, k)
    return quick_select(larger, k - len(smaller) - 1)