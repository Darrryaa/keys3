def par_1():
    '''
    Function that calculates tax per parent.
    '''
    amount = 0
    amount_tax = 0
    amount_diff = 0
    sum_tax = 0
    amount_month = []
    for month in range(1, 12 + 1):
        value = float(input())
        amount += value
        amount_month.append((value))
    print(round(amount, 2))
    for month in range(1, 12 + 1):
        diff = 0
        taxxist = 0
        tax = float(input())
        amount_tax += tax
        diff = amount_month[month-1] - tax
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
    print(round(amount_tax, 2))
    print(round(amount_diff, 2))
    print(round(sum_tax, 2))
    print(round(sum_tax / 12, 2))


par_1()
