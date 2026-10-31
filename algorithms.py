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
