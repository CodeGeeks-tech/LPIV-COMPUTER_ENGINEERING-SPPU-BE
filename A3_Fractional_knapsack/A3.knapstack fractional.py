def fractional_knapsack():
    n = int(input("Enter number of items: "))

    weights = []
    values = []

    # Taking input for weights and values
    for i in range(n):
        w = float(input(f"Enter weight of item {i+1}: "))
        v = float(input(f"Enter value of item {i+1}: "))
        weights.append(w)
        values.append(v)

    capacity = float(input("Enter capacity of knapsack: "))
    res = 0.0  # To store final result

    # Sort by value-to-weight ratio in descending order
    for weight, value in sorted(zip(weights, values), key=lambda x: x[1] / x[0], reverse=True):
        if capacity <= 0:
            break

        if weight <= capacity:
            # Take full item
            res += value
            capacity -= weight
        else:
            # Take fractional part
            res += value * (capacity / weight)
            capacity = 0

    print(f"\nMaximum value in Knapsack = {res:.2f}")

if __name__ == "__main__":
    fractional_knapsack()


"""
================ SAMPLE INPUT =================

Enter number of items: 3
Enter weight of item 1: 10
Enter value of item 1: 60
Enter weight of item 2: 20
Enter value of item 2: 100
Enter weight of item 3: 30
Enter value of item 3: 120
Enter capacity of knapsack: 50


================ SAMPLE OUTPUT ================

Maximum value in Knapsack = 240.00

(Explanation: take full items 1 and 2, take 2/3rd of item 3)

================================================
"""