import LavaAPI
import time

lavaToken = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1aWQiOiI0YWU2YjA5OC0wMGQyLWRhYmYtOGQ0Zi1kNDhiYjUxNmVkYWYiLCJ0aWQiOiJlMDIwMGM1OS0xOWNkLWI2NzgtMWIzYS01MGM5MmMxMWI2ZjUifQ.apPiGeesuwUMNaWbmET7yp8moAv039skRJ2aIsppV94"
lavaAccountID = "R10007689"

print(LavaAPI.CheckWallet(lavaToken))
if LavaAPI.CheckWallet(lavaToken):
    #  Узнаем баланс кошелька
    print(LavaAPI.WalletBalance(lavaToken, "RUB"))

    #  Создаем счет
    createBill = LavaAPI.InvoiceCreate(lavaToken, lavaAccountID, 10, comment="DBD-4KDAS891")
    print("Ссылка для оплаты: ", createBill["url"])

    #  Проверяем каждые 5 секунд
    while True:
        if LavaAPI.InvoiceInfo(lavaToken, createBill["id"])["invoice"]["status"] == "success":
            print("Деньги пришли")
            break
        time.sleep(5)