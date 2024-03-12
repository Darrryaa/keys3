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
                income_value = float(input("Введите доход за месяц: "))
                total_income += income_value
                monthly_incomes.append(income_value)

            for month in range(1, 12 + 1):
                tax_free_allowance = float(input("Введите сумму налогового вычета за месяц: "))
                total_tax_free += tax_free_allowance
                taxable_income = monthly_incomes[month - 1] - tax_free_allowance

                if taxable_income > 406751:
                    tax_rate = 0.396
                elif 405101 < taxable_income <= 406751:
                    tax_rate = 0.35
                elif 186351 < taxable_income <= 405101:
                    tax_rate = 0.33
                elif 89351 < taxable_income <= 186351:
                    tax_rate = 0.28
                elif 36901 < taxable_income <= 89351:
                    tax_rate = 0.25
                elif 9075 < taxable_income <= 36901:
                    tax_rate = 0.15
                else:
                    tax_rate = 0.1

                tax_paid = taxable_income * tax_rate
                total_taxed += (taxable_income - tax_paid)
                total_tax_paid += tax_paid

            print("Сумма годового дохода, не облагаемого налогом:", round(total_tax_free, 2))
            print("Сумма годового дохода, облагаемого налогом:", round(total_taxed, 2))
            print("Величина годового налога:", round(total_tax_paid, 2))
            print("Ежемесячный налоговый платёж: ", round(total_tax_paid / 12, 2))
            
def universal_calc(num, count, nonTax):
            # Вся сумма с которой мы должны заплатить налоги
            taxable = count - nonTax
            # Общий налог
            allTax = 0

            for elem in YEAR_TAX:
                if elem[num] < taxable:
                    # Сколько денег осталось с которых не уплачен налог
                    taxable = taxable - elem[num]
                    allTax += elem[num] * (elem[0] * 0.01)
                else:
                    taxable = taxable
                    allTax += taxable * (elem[0] * 0.01)
                    return allTax

            # Когда мы понимаем, что наша сумма превышает всю таблицу и мы не досчитали до конца, выйдя из таблицы
            # мы возьмем оставшиеся деньги и посчитаем их по самому максимальному проценту в таблице, так как до этого
            # мы шли в таблице от минимального процента к максимальному
            allTax += taxable * (YEAR_TAX[6][0] * 0.01)
            return allTax
 
def lab_1():

            count = 0
            for elem in MONTH:
                count += int(input(f"Доход в {elem} (USD): "))

            print(f"Сумма годового дохода: ${count}")

            print("Укажите величину годовой суммы, не облагаемой налогом: ")

            nonTax = 0
            for elem in MONTH:
                nonTax += int(input(f"Сумма не облагаемая налогом в январе {elem} (USD): "))

            print(f"Сумма годового дохода, не облагаемого налогом: ${nonTax}")

            if nonTax > count:
                print(
                    f"сумма не облагаемая налогом не может быть больше чем облагаемая, ошибка в веденных данных! ({nonTax} > {count})")
                return

            print(f"Сумма годового дохода, облагаемого налогом: ${count - nonTax}")

            allTax = universal_calc(num, count, nonTax)

            print(f"Величина годового налога: {int(allTax)}")

            allTax = allTax / 12

            print(f"Ежемесячный налоговый платеж: {int(allTax)}")

def one_parent():
            '''
            Function that calculates tax per parent.
            '''
            amount = 0
            amount_tax = 0
            amount_diff = 0
            no_tax = 0
            wth_tax = 0
            sum_tax = 0
            amount_month = []
            for month in range(1, 12 + 1):
                value = float(input())
                amount += value
                amount_month.append((value))
                amount_month.append(value)
            print(round(amount, 2))
            for month in range(1, 12 + 1):
                diff = 0
                taxxist = 0
                tax = float(input())
                amount_tax += tax
                diff = amount_month[month - 1] - tax
                amount_diff += diff
                progress_tax = 0
                tax_free = float(input())
                no_tax += tax_free
                diff = amount_month[month - 1] - tax_free
                wth_tax += diff
                if diff > 432201:
                    taxxist += (diff - 432201) * 0.396
                    progress_tax += (diff - 432201) * 0.396
                    diff = 432201
                if 405101 < diff <= 432201:
                    taxxist += (diff - 405101) * 0.35
                    progress_tax += (diff - 405101) * 0.35
                    diff = 405101
                if 206601 < diff <= 405101:
                    taxxist += (diff - 206601) * 0.33
                    progress_tax += (diff - 206601) * 0.33
                    diff = 206601
                if 127551 < diff <= 206601:
                    taxxist += (diff - 127551) * 0.28
                    progress_tax += (diff - 127551) * 0.28
                    diff = 127551
                if 49401 < diff <= 127551:
                    taxxist += (diff - 49401) * 0.25
                    progress_tax += (diff - 49401) * 0.25
                    diff = 49401
                if 12951 < diff <= 49401:
                    taxxist += (diff - 12951) * 0.15
                    progress_tax += (diff - 12951) * 0.15
                    diff = 12951
                if 0 < diff <= 12951:
                    taxxist += diff * 0.1
                sum_tax += taxxist
            print(round(amount_tax, 2))
            print(round(amount_diff, 2))
            #progress_tax += diff * 0.1  #!
                #sum_tax += progress_tax         #!
            print(round(no_tax, 2))
            print(round(wth_tax, 2))
            print(round(sum_tax, 2))
            print(round(sum_tax / 12, 2))

def main():
    max_month = 12
    MONTH = ['январе', 'феврале', 'марте', 'апреле', 'мае', 'июне', 'июле', 'августе', 'сентябре', 'октябре', 'ноябре',
                 'декабре']
    YEAR_TAX = [[10, 9075, 18150, 12950],
                [15, 36900, 73800, 49400],
                [25, 89350, 148850, 127550],
                [28, 186350, 226850, 206600],
                [33, 405100, 405100, 405100],
                [35, 406750, 457600, 432200],
                [39.6, 406751, 457601, 432201]]

    print("Укажите категорию налогоплательщика: ")
    num = 0
    while (num < 1 or num > 3):
        print("1. Субъект")
        print("2. Супружеская пара")
        print("3. Один родитель")

        num = int(input("Введите значение [1-3]:"))

    print("Укажите величину годового дохода: ")

    if num == 1:
        
    elif num == 2:
        
    else:

        one_parent()

if __name__ == '__main__':
   main()
