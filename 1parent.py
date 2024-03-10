def one_parent():
    '''
    Function that calculates tax per parent.
    '''
    amount = 0
    no_tax = 0
    wth_tax = 0
    sum_tax = 0
    amount_month = []
    for month in range(1, 12 + 1):
        value = float(input())
        amount += value
        amount_month.append(value)
    print(round(amount, 2))
    for month in range(1, 12 + 1):
        progress_tax = 0
        tax_free = float(input())
        no_tax += tax_free
        diff = amount_month[month-1] - tax_free
        wth_tax += diff
        if diff > 432201:
            progress_tax += (diff - 432201) * 0.396
            diff = 432201
        if 405101 < diff <= 432201:
            progress_tax += (diff - 405101) * 0.35
            diff = 405101
        if 206601 < diff <= 405101:
            progress_tax += (diff - 206601) * 0.33
            diff = 206601
        if 127551 < diff <= 206601:
            progress_tax += (diff - 127551) * 0.28
            diff = 127551
        if 49401 < diff <= 127551:
            progress_tax += (diff - 49401) * 0.25
            diff = 49401
        if 12951 < diff <= 49401:
            progress_tax += (diff - 12951) * 0.15
            diff = 12951
        if 0 < diff <= 12951:
            progress_tax += diff * 0.1
        sum_tax += progress_tax
    print(round(no_tax, 2))
    print(round(wth_tax, 2))
    print(round(sum_tax, 2))
    print(round(sum_tax / 12, 2))


one_parent()
