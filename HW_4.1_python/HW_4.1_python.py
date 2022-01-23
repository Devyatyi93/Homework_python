# while True:
        # i_rub=int(input())
        # i_usd=i_rub/77.59
        # print("Ты ввёл", i_rub, "руб.")
        # print("конвертированная сумма в USD =", i_usd)

while True:
        i_rub = int(input())
        i_usd = round(i_rub / 77.59, 2)
        i_eur = round(i_rub / 88.05, 2)
        i_chf = round(i_rub / 85.10, 2)
        i_gbr = round(i_rub / 105.17, 2)
        i_cny = round(i_rub / 12.24, 2)
        print("Ты ввёл", i_rub, "руб.")
        print("конвертированная сумма в USD =", i_usd)
        print("конвертированная сумма в EUR =", i_eur)
        print("конвертированная сумма в CHF =", i_chf)
        print("конвертированная сумма в GBP =", i_gbr)
        print("конвертированная сумма в CNY =", i_cny)




while True:
        i_r = input()
        try:
                i_rub=int(i_r)
                if i_rub>0:
                        i_usd = round(i_rub / 77.59, 2)
                        i_eur = round(i_rub / 88.05, 2)
                        i_chf = round(i_rub / 85.10, 2)
                        i_gbr = round(i_rub / 105.17, 2)
                        i_cny = round(i_rub / 12.24, 2)
                        print("Ты ввёл", i_rub, "руб.")
                        print("конвертированная сумма в USD =", i_usd)
                        print("конвертированная сумма в EUR =", i_eur)
                        print("конвертированная сумма в CHF =", i_chf)
                        print("конвертированная сумма в GBP =", i_gbr)
                        print("конвертированная сумма в CNY =", i_cny)
                else:
                        print("Введите положительное число.")
        except:
                if i_r=="":
                        print("Вы ввели пустое поле. Введите число.")
                else:
                        print("Вы ввели не число. Введите число.")





i = ['USD', 'EUR', 'CHF', 'GBP', 'CNY']

while True:
    print("Выберите валюту из", i)
    ii = input()
    print("Введите сумму")
    i_r = input()
    try:
        i_rub=int(i_r)


        if i_rub>0:
            if ii == 'USD' or ii == 'usd':
                print("Вы ввели сумму", i_rub, "и валюту РУБ.")
                i_usd = round(int(i_rub) / 77.59, 2)
                print("конвертированная сумма в", ii, "=", i_usd)
            elif ii == 'EUR' or ii == 'eur':
                print("Вы ввели сумму", i_rub, "и валюту РУБ.")
                i_eur = round(i_rub / 88.05, 2)
                print("конвертированная сумма в", ii, "=", i_eur)
            elif ii == 'CHF' or ii == 'chf':
                print("Вы ввели сумму", i_rub, "и валюту РУБ.")
                i_chf = round(i_rub / 85.10, 2)
                print("конвертированная сумма в", ii, "=", i_chf)
            elif ii == 'GBR' or ii == 'gbr':
                print("Вы ввели сумму", i_rub, "и валюту РУБ.")
                i_gbr = round(i_rub / 105.17, 2)
                print("конвертированная сумма в", ii, "=", i_gbr)
            elif ii == 'CNY' or ii == 'cny':
                print("Вы ввели сумму", i_rub, "и валюту РУБ.")
                i_cny = round(i_rub / 12.24, 2)
                print("конвертированная сумма в", ii, "=", i_cny)

        else:
            print("Введите положительное число.")

    except:
        if i_r=="":
            print("Вы ввели пустое поле. Введите число.")
        else:
          print("Вы ввели не число. Введите число.")



