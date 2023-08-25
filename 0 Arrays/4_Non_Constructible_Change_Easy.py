'''
Description:
    Given an array of positive integers representing the values of coins in your
    possession, write a function that returns the minimum amount of change (the
    minimum sum of money) that you cannot create. The given coins can have
    any positive integer value and aren't necessarily unique (i.e., you can have
    multiple coins of the same value).

    For example, if you're given coins = [1, 2, 5], the minimum
    amount of change that you can't create is 4. If you're given no
    coins, the minimum amount of change that you can't create is 1.

Sample I/O:
    coins = [5, 7, 1, 1, 2, 3, 22]
    ouput = 20

-> Make sure to make it as optimized as possible, both time and space complexity wise.
-> Take a deep breath, put aside your 'imposter-self', and give it a go ;)
'''

def nonConstructibleChange(coins):
    coins.sort()
    currentMaxChange = 0

    for coin in coins:
        if coin > currentMaxChange + 1:
            break
        currentMaxChange += coin
        
    return currentMaxChange + 1


print(nonConstructibleChange([5, 7, 1, 1, 2, 3, 22]))
'''
Analysis:
        Start by sorting the array, as we need MINIMUM change, we can start by left side
    with least values (of coins in the array).    

    To understand the trick to this problem, consider the following example:
    coins = [1, 2, 4]. 
    With this set of coins, we can create 1, 2, 3, 4, 5, 6, 7 cents worth of change. Now, if we were to add a coin of value 9 to this set, we would not be able to 
    create 8 cents. However, if we were to add a coin of value 7, we would be able to create 8 cents, and we would also be able to create all values of change from 1 to
    15. Why is this the case?
    
    To cut is short - 
    We can create change upto previous-constructible-change + new-coin in the set;
    but the new coin should be greate than the previous-constructible-change not-more-than 1.

    as for [1,2,4], I can create max of 7, so 8th can't be created
    If I were to add a 9, the difference 9 - 7 is 2, which is > 1. So, it will be 
    the lastMax + 1, which can't be created.

    Time | Space Complexity
    This is the great trick, but it works with sorted array of coins.
    So, We are performing two costly operations:
        -> Sorting | O(nlogn)
        -> Iteration | O(n)

    So, time complexity is O(nlogn)

    And no extra space is used, so it is O(1)

    T O(nlogn) | S O(1)
'''
