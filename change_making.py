coin_set = [1, 4, 9]
target = 59

def getVal(A, i):
    if i<0:
        return 10000000000000000
    else:
        return A[i]

def min_coins(n):
    A = ['empty'] * (n+1);
    A[0] = 0
    #solution build contains all values leading up to and including the target
    #and their associated min number of coins
    solution_build = {0: 0}
    for i in range(1, n+1):
        minimum = 1 + min(getVal(A, i-coin_set[0]), getVal(A, i-coin_set[1]), getVal(A, i-coin_set[2]))
        solution_build[i] = minimum
        A[i] = minimum

    print("Minimum number of coins needed for target " + str(n) + " is " + str(solution_build.get(n)))

    coins = getCoins(n)

    print("The coins needed are: " + str(coins))
    return A[n]


def getCoins(target):
    coins = []

    while(target>=coin_set[2]):
        coins.append(str(coin_set[2]))
        target = target - coin_set[2]
    while(target>=coin_set[1]):
        coins.append(str(coin_set[1]))
        target = target - coin_set[1]
    coins.append(str(target*coin_set[0]))
    return coins

min_coins(target)
