from main import cacl

while True:
        i_r = input()
        try:
                i_ru=int(i_r)
                if i_ru>0:
                        cacl(i_ru)
                        # i_usd = round(i_rub / 77.59, 2)
                        # i_eur = round(i_rub / 88.05, 2)
                        # i_chf = round(i_rub / 85.10, 2)
                        # i_gbr = round(i_rub / 105.17, 2)
                        # i_cny = round(i_rub / 12.24, 2)
                        # print("Ты ввёл", i_rub, "руб.")
                        # print("конвертированная сумма в USD =", i_usd)
                        # print("конвертированная сумма в EUR =", i_eur)
                        # print("конвертированная сумма в CHF =", i_chf)
                        # print("конвертированная сумма в GBP =", i_gbr)
                        # print("конвертированная сумма в CNY =", i_cny)
                else:
                        print("Введите положительное число.")
        except:
                if i_r=="":
                        print("Вы ввели пустое поле. Введите число.")
                else:
                        print("Вы ввели не число. Введите число.")
