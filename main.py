# Case-study #3
# Developers: Denisova D., Ukhov S., Simonov A., Zlygosteva M.
#
import ru_local as ru

def one_person():

    total_income = 0
    total_tax_free = 0
    total_taxed = 0
    total_tax_paid = 0
    monthly_incomes = []

    for month in range(1, 12 + 1):
        income_value = float(input(f'{ru.INCOME_IN} {ru.NAME[month-1]} (USD): '))
        total_income += income_value
        monthly_incomes.append(income_value)

    for month in range(1, 12 + 1):
        tax_rate = 0
        tax_free_allowance = float(input(f'{ru.AMOUNT_TAX_FREE_IN} {ru.NAME[month-1]} (USD): '))
        total_tax_free += tax_free_allowance
        taxable_income = monthly_incomes[month - 1] - tax_free_allowance
        total_taxed += taxable_income
        
        if taxable_income > 406751:
            tax_rate += (taxable_income - 406751) * 0.396
            taxable_income = 406751
        if 405101 < taxable_income <= 406751:
            tax_rate += (taxable_income - 406751) * 0.35
            taxable_income = 405101
        if 186351 < taxable_income <= 405101:
            tax_rate += (taxable_income - 406751) * 0.33
            taxable_income = 186351
        if 89351 < taxable_income <= 186351:
            tax_rate += (taxable_income - 406751) * 0.28
            taxable_income = 89351
        if 36901 < taxable_income <= 89351:
            tax_rate += (taxable_income - 406751) * 0.25
            taxable_income = 36901
        if 9075 < taxable_income <= 36901:
            tax_rate += (taxable_income - 406751) * 0.15
            taxable_income = 9075
        if 0 < taxable_income < 9075:
            tax_rate += taxable_income * 0.1
        total_tax_paid += tax_rate

    print(f'{ru.AMOUNT_OF_ANNUAL_INCOME_NOT_TAXED} {round(total_tax_free, 2)}')
    print(f'{ru.AMOUNT_OF_ANNUAL_INCOME_TAXABLE_INCOME} {round(total_taxed, 2)}')
    print(f'{ru.ANNUAL_TAX_AMOUNT} {round(total_tax_paid, 2)}')
    print(f'{ru.MONTHLY_TAX_PAYMENT} {round(total_tax_paid / 12, 2)}')

 
def married_couple():
    amount = 0
    no_tax = 0
    wth_tax = 0
    sum_tax = 0
    amount_month = []
    for month in range(1, 12 + 1):
        value = float(input(f'{ru.INCOME_IN} {ru.NAME[month - 1]} (USD): '))
        amount += value
        amount_month.append(value)
    print(f'{ru.AMOUNT_OF_ANNUAL_INCOME} ${round(amount, 2)}')
    for month in range(1, 12 + 1):
        progress_tax = 0
        tax_free = float(input(f'{ru.AMOUNT_TAX_FREE_IN} {ru.NAME[month - 1]} (USD): '))
        no_tax += tax_free
        diff = amount_month[month - 1] - tax_free
        wth_tax += diff
        if diff > 457601:
            progress_tax += (diff - 457601) * 0.396
            diff = 457601
        if 405101 < diff <= 457601:
            progress_tax += (diff - 405101) * 0.35
            diff = 405101
        if 226851 < diff <= 405101:
            progress_tax += (diff - 226851) * 0.33
            diff = 226851
        if 148851 < diff <= 226851:
            progress_tax += (diff - 148851) * 0.28
            diff = 148851
        if 73801 < diff <= 148851:
            progress_tax += (diff - 73801) * 0.25
            diff = 73801
        if 18151 < diff <= 73801:
            progress_tax += (diff - 18151) * 0.15
            diff = 18151
        if 0 < diff <= 18151:
            progress_tax += diff * 0.1
        sum_tax += progress_tax
    print(f'{ru.AMOUNT_OF_ANNUAL_INCOME_NOT_TAXED} ${round(no_tax, 2)}')
    print(f'{ru.AMOUNT_OF_ANNUAL_INCOME_TAXABLE_INCOME} ${round(wth_tax, 2)}')
    print(f'{ru.ANNUAL_TAX_AMOUNT} {round(sum_tax, 2)}')
    print(f'{ru.MONTHLY_TAX_PAYMENT} {round(sum_tax / 12, 2)}')
    
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
        value = float(input(f'{ru.INCOME_IN} {ru.NAME[month-1]} (USD): '))
        amount += value
        amount_month.append(value)
    print(f'{ru.AMOUNT_OF_ANNUAL_INCOME} ${round(amount, 2)}')
    for month in range(1, 12 + 1):
        progress_tax = 0
        tax_free = float(input(f'{ru.AMOUNT_TAX_FREE_IN} {ru.NAME[month-1]} (USD): '))
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
    print(f'{ru.AMOUNT_OF_ANNUAL_INCOME_NOT_TAXED} ${round(no_tax, 2)}')
    print(f'{ru.AMOUNT_OF_ANNUAL_INCOME_TAXABLE_INCOME} ${round(wth_tax, 2)}')
    print(f'{ru.ANNUAL_TAX_AMOUNT} {round(sum_tax, 2)}')
    print(f'{ru.MONTHLY_TAX_PAYMENT} {round(sum_tax / 12, 2)}')

def main():
    max_month = 12
    print(f'{ru.SPECIFY_CATEGORY_OF_TAXPAYER}')
    num = 0
    while (num < 1 or num > 3):
        print(f' 1. {ru.SUBJECT}')
        print(f' 2. {ru.MARRIED_COUPLE}')
        print(f' 3. {ru.ONE_PARENT}')

        num = int(input(f'{ru.ENTER_VALUE}[1-3]: '))

    if num == 1:
        one_person()
    elif num == 2:
        married_couple()
    else:
        one_parent()

if __name__ == '__main__':
   main()
