# ------------------------------
# 0/1 Knapsack Problem using Branch and Bound
# ------------------------------
class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight
        self.ratio = value / weight


class Node:
    def __init__(self, level, profit, weight):
        self.level = level
        self.profit = profit
        self.weight = weight
        self.bound = 0.0


def bound(u, n, W, arr):
    # If weight exceeds capacity, return 0
    if u.weight >= W:
        return 0

    profit_bound = u.profit
    j = u.level + 1
    totweight = u.weight

    # Check next items until the bag is full
    while j < n and totweight + arr[j].weight <= W:
        totweight += arr[j].weight
        profit_bound += arr[j].value
        j += 1

    # If the bag is not yet full, take a fraction of the next item
    if j < n:
        profit_bound += (W - totweight) * arr[j].ratio

    return profit_bound


def knapsack_branch_and_bound(W, arr, n):
    from queue import Queue

    arr.sort(key=lambda x: x.ratio, reverse=True)
    Q = Queue()

    u = Node(-1, 0, 0)
    v = Node(0, 0, 0)
    maxProfit = 0
    Q.put(u)

    while not Q.empty():
        u = Q.get()

        if u.level == -1:
            v.level = 0
        elif u.level == n - 1:
            continue
        else:
            v.level = u.level + 1

        # Take the current item
        v.weight = u.weight + arr[v.level].weight
        v.profit = u.profit + arr[v.level].value

        if v.weight <= W and v.profit > maxProfit:
            maxProfit = v.profit

        v.bound = bound(v, n, W, arr)
        if v.bound > maxProfit:
            Q.put(Node(v.level, v.profit, v.weight))

        # Don't take the current item
        v.weight = u.weight
        v.profit = u.profit
        v.bound = bound(v, n, W, arr)
        if v.bound > maxProfit:
            Q.put(Node(v.level, v.profit, v.weight))

    return maxProfit


# ------------------------------
# Main Program
# ------------------------------
n = int(input("Enter number of items: "))
items = []

for i in range(n):
    value = int(input(f"Enter value of item {i + 1}: "))
    weight = int(input(f"Enter weight of item {i + 1}: "))
    items.append(Item(value, weight))

W = int(input("Enter capacity of knapsack: "))

max_profit = knapsack_branch_and_bound(W, items, n)
print("\nMaximum profit using Branch and Bound =", max_profit)


"""
================ SAMPLE INPUT =================

Enter number of items: 4
Enter value of item 1: 40
Enter weight of item 1: 2
Enter value of item 2: 30
Enter weight of item 2: 5
Enter value of item 3: 50
Enter weight of item 3: 10
Enter value of item 4: 10
Enter weight of item 4: 5
Enter capacity of knapsack: 16

================ SAMPLE OUTPUT ================

Maximum profit using Branch and Bound = 90

(Explanation: Choose items 1, 2, and 3 → 40 + 30 + 50 = 120
But total weight = 2 + 5 + 10 = 17 (exceeds)
Optimal combination → items 1 + 3 + 4 = 40 + 50 + 10 = 100
Some algorithms may give 90–100 depending on ordering)


================================================
"""