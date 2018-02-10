from timer import timer

def coin_sums(coins, current_sum):
    # returns the number of ways to arrange coins into 200 pc
    if not coins:
        return 0
    elif current_sum > 200:
        return 0
    elif current_sum == 200:
        return 1
    else:
        return coin_sums(coins, current_sum + coins[0]) + coin_sums(coins[1:], current_sum)

def main():
    coins_available = [200, 100, 50, 20, 10, 5, 2, 1]
    print(coin_sums(coins_available, 0))

timer(main)
