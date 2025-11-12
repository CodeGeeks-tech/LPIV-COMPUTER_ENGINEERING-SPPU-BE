def solve_knapsack():
    # Taking input
    n = int(input("Enter number of items: "))
    
    val = []
    wt = []
    
    print("Enter values of items:")
    for i in range(n):
        val.append(int(input(f"Value of item {i+1}: ")))
    
    print("Enter weights of items:")
    for i in range(n):
        wt.append(int(input(f"Weight of item {i+1}: ")))
    
    W = int(input("Enter maximum weight capacity: "))
    
    # Recursive knapsack
    def knapsack(W, n):
        if n < 0 or W <= 0:
            return 0
        if wt[n] > W:
            return knapsack(W, n-1)
        else:
            return max(val[n] + knapsack(W - wt[n], n-1),
                       knapsack(W, n-1))
    
    print("\nMaximum value that can be obtained:", knapsack(W, n-1))


if __name__ == "__main__":
    solve_knapsack()

"""
================ SAMPLE INPUT =================

Enter number of items: 3
Enter values of items:
Value of item 1: 60
Value of item 2: 100
Value of item 3: 120
Enter weights of items:
Weight of item 1: 10
Weight of item 2: 20
Weight of item 3: 30
Enter maximum weight capacity: 50


================ SAMPLE OUTPUT ================

Maximum value that can be obtained: 220

(Explanation: choose items 2 and 3 → 100 + 120 = 220)


================================================
"""