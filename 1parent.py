def par_1():
    '''
    The function determines the annual tax-free amount.
    '''
    amount = 0
    amount_tax = 0
    amount_diff = 0
    sum_tax = 0
    for month in range(1, 12 + 1):
        diff = 0
        taxxist = 0
        value = float(input())
        tax = float(input())
        amount += value
        amount_tax += tax
        diff = value - tax
        amount_diff += diff
        if diff > 432201:
            taxxist += (diff - 432201) * 0.396
            diff = 432201
        if 405101 < diff <= 432201:
            taxxist += (diff - 405101) * 0.35
            diff = 405101
        if 206601 < diff <= 405101:
            taxxist += (diff - 206601) * 0.33
            diff = 206601
        if 127551 < diff <= 206601:
            taxxist += (diff - 127551) * 0.28
            diff = 127551
        if 49401 < diff <= 127551:
            taxxist += (diff - 49401) * 0.25
            diff = 49401
        if 12951 < diff <= 49401:
            taxxist += (diff - 12951) * 0.15
            diff = 12951
        if 0 < diff <= 12951:
            taxxist += diff * 0.1
        sum_tax += taxxist
    return amount, amount_tax, amount_diff, sum_tax, sum_tax / 12


print(par_1())
