def cacc(ii, i_rub):
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