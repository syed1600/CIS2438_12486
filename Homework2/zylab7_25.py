# Syed Ali
# 1799248

# defining function and calculating total using the fewest coins
def exact_change(user_total):
    numb_dollars = user_total // 100
    user_total %= 100
    numb_quarters = user_total // 25
    user_total %= 25
    numb_dimes = user_total // 10
    user_total %= 10
    numb_nickels = user_total // 5
    user_total %= 5
    numb_pennies = user_total
    return numb_dollars, numb_quarters, numb_dimes, numb_nickels, numb_pennies


# from the lab
if __name__ == '__main__':
    input_val = int(input())
    num_dollars, num_quarters, num_dimes, num_nickels, num_pennies = exact_change(input_val)

    if input_val == 0:
        print('no change')
    else:
        if num_dollars > 1:
            print(num_dollars, 'dollars')
        elif num_dollars == 1:
            print(num_dollars, 'dollar')
        if num_quarters > 1:
            print(num_quarters, 'quarters')
        elif num_quarters == 1:
            print(num_quarters, 'quarter')
        if num_dimes > 1:
            print(num_dimes, 'dimes')
        elif num_dimes == 1:
            print(num_dimes + 'dime')
        if num_nickels > 1:
            print(num_nickels, 'nickels')
        elif num_nickels == 1:
            print(num_nickels, 'nickel')
        if num_pennies > 1:
            print(num_pennies, 'pennies')
        elif num_pennies == 1:
            print(num_pennies, 'penny')
