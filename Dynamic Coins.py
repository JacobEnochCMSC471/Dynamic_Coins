import math


# CMSC441 Exam 2 Group 3


# m is size of coins array (number of different coins)
def num_coins_topdown(N, denominations):  # Working correctly, regular recursion, no memoization
    if N == 0:
        return 0

    min_coins = math.inf

    for i in denominations:  # for each denomination possible for current value of N, try all combinations, take lowest number of coins
        if i <= N:
            curr_min = 1 + num_coins_topdown(N - i, denominations)

            if curr_min < min_coins:
                min_coins = curr_min

    return min_coins


def num_coins_topdown_starter(N, denominations):
    opt_list = [math.inf for _ in range(N + 1)]  # Create opt_list with N slots in list
    opt_list[0] = 0
    min_coins = num_coins_topdown_memoized(N, denominations, opt_list)  # Call memoized version of num_coins
    return min_coins


def num_coins_topdown_memoized(N, denominations, opt_memo):
    if N == 0:  # Recursion base case - remaining money to convert = 0
        return opt_memo[0]  # Return 0

    elif opt_memo[N] != math.inf:  # If the opt_memo has had it's value changed, use this instead of recursing deeper
        return opt_memo[N]

    min_coins = math.inf  # Min coins should initialize as something large

    for i in denominations:  # Search every possibility of coins for every value of N
        if i <= N:
            curr_min = 1 + num_coins_topdown_memoized(N - i, denominations, opt_memo)  # Find current min for N

            if curr_min < min_coins:  # Find lowest value in list (optimal min for this value of N)
                min_coins = curr_min
                opt_memo[N] = min_coins  # Add min value to opt memo for look-up later

    return min_coins


def num_coins_bottom_up(N, denominations):  # Start from simplest problem first, solve, use solutions to solve harder problems
    opt_list = [math.inf for _ in range(N + 1)]  # Create opt_list with N slots in list

    for i in range(N + 1):  # Outer loop: current value of N
        if i == 0:  # If N is 0 then opt number of coins is 0
            opt_list[0] = 0
            continue  # Move on to N = 1 if possible

        for j in denominations:  # Inner loop: current denomination
            if j <= i:  # Only look at denominations that are able to go into i
                current_min = 1 + opt_list[i - j]  # Apply recursive formula but on list rather than recursion

                if current_min < opt_list[i]:  # If the current minimum is less than item in corresponding opt_list index, replace
                    opt_list[i] = current_min

    return opt_list[N]  # Optimal number of coins is located at last index


curr_denominations = [1, 7, 12, 26, 55]
value = 95
# ("Top-down non-memoized: " + str(num_coins_topdown(value, curr_denominations))) # This takes forever for bigger denominations, don't use!
print("Top-down Memoized:" + str(num_coins_topdown_starter(value, curr_denominations)))  # Top-down, memoized version
print("Bottom-Up Iterative: " + str(num_coins_bottom_up(value, curr_denominations)))  # Bottom-up iterative version

# 2C: d2 <= c2 < d3
# 5 <= c2 < 10 as example
