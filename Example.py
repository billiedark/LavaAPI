import LavaAPI

token = "MY_TOKEN"

if LavaAPI.CheckWallet(token):

    #  Узнаем баланс кошелька
    print(LavaAPI.WalletBalance(token, "RUB"))

    #  Ждем перевод с нужным комментарием
    while True:
        transfers = LavaAPI.TransactionsList("MY_TOKEN", "R10007689", type="transfer", limit=1)[0]
        if transfers["comment"] == "BILL-ID-3201821" and transfers["amount"] == "500":
            print("Платеж найден")
            break