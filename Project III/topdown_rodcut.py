'''
Purpose : Implement a Top Down approach to the Rod Cutting Algorithm
Author  : Hameed Abdul
Date    : 4/1/2018
'''
import numpy as np

# Numpy array to store pipe value by length (0 - 10)
# Numpy array (0 through 10) just for output
prices = np.array([0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 20])
rod_lengths = np.arange(11)

def memoized_topdown_rodcut(prices, curr_rod_length):
    """
    Initializes array of 11 elements ( 0 to n+1). Elements 1 through n+1 = -9999
    :param prices: array of values correlated to each rod's length
    :param curr_rod_length: current rod length
    :return: Calls the coupled function and returns correct value for specifed index
    """
    # Array to store max profit for each length (0 to n+1)
    # Set the min value for elements 1 through n+1
    rodcut_profit = np.repeat(-999, curr_rod_length + 1)
    rodcut_profit[0] = 0

    # Updates each index of rodcut_profit accordingly
    # Return result in array format
    _memoized_topdown_rodcut(prices, curr_rod_length, rodcut_profit)
    return rodcut_profit 

def _memoized_topdown_rodcut(prices, curr_rod_length, rodcut_profit):
    """
    :param prices: array of values correlated to each rod's length
    :param curr_rod_length:  current rod length
    :param rodcut_profit:
    :return:
    """
    if curr_rod_length != 0:
        # Initialize curr_max to a negative int
        curr_max = -999
        # Loop from 1 to 10
        for i in range(1, curr_rod_length + 1):
            # Add the current index's price to each unique permutation of the current length possible
            # Select the Maximum value and return
            val_to_check = prices[i] + _memoized_topdown_rodcut(prices, curr_rod_length - i, rodcut_profit)
            curr_max = max(curr_max, val_to_check)
        rodcut_profit[i] = curr_max
        # So just return the current rod's max profit
        return curr_max
    # Else return 0
    return 0

# Run roddcutting and Store results
optimal_profit = memoized_topdown_rodcut(prices, 10)

# Print results and relevant info
print('Rod Length:\t\t\t', rod_lengths)
print('Prices:\t\t\t\t', prices)
print("===================================================================\nMax Profit: \t\t\t", optimal_profit)
