def solve_knapsack_tabulation():
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

    # dp[i][w] = maximum value with first i items and weight limit w
    dp = [[0] * (W + 1) for _ in range(n + 1)]

    # Build DP table
    for i in range(1, n + 1):
        for w in range(1, W + 1):

            if wt[i - 1] > w:
                dp[i][w] = dp[i - 1][w]       # item cannot be taken
            else:
                dp[i][w] = max(
                    val[i - 1] + dp[i - 1][w - wt[i - 1]],  # include
                    dp[i - 1][w]                            # exclude
                )

    print("\nMaximum value using DP:", dp[n][W])


if __name__ == "__main__":
    solve_knapsack_tabulation()

