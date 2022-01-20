import requests


#  Quick token validation check. Returns to Boolean
def CheckWallet(token):
    headers = {
        "Authorization": token,
    }
    answer = requests.get("https://api.lava.ru/test/ping", headers=headers)
    if answer.json()["status"] == True:
        return True
    else:
        return False


#  Detailed verification of the token. Returns either True or String
def CheckWalletDetails(token):
    headers = {
        "Authorization": token,
    }
    answer = requests.get("https://api.lava.ru/test/ping", headers=headers)
    if answer.json()["status"] == True:
        return True
    else:
        return answer.json()["message"]


#  Getting the balance of the wallet. Returns to Float
def WalletBalance(token, currency):
    if currency not in ["USD", "EUR", "RUB"]:
        return "Invalid currency"
    if not CheckWallet(token):
        return "Invalid token"
    headers = {
        "Authorization": token,
    }
    answer = requests.get("https://api.lava.ru/wallet/list", headers=headers)
    return answer.json()[0]["balance"]


#  Withdrawing funds from the system. Returns to Boolean or String
def WithdrawCreate(token, account, amount, service, walletBen):
    if not CheckWallet(token):
        return "Invalid token"
    headers = {
        "Authorization": token,
    }
    data = {
        "account": account,
        "amount": amount,
        "service": service,
        "wallet_to": walletBen
    }
    answer = requests.post("https://api.lava.ru/withdraw/create", headers=headers, data=data)
    if answer.json()["status"] == "success":
        return True
    else:
        return answer.json()["message"]


#  Transfer of funds between accounts. Returns to Boolean or String
def TransferCreate(token, account, amount, accountBen):
    if not CheckWallet(token):
        return "Invalid token"
    headers = {
        "Authorization": token,
    }
    data = {
        "account_from": account,
        "account_to": accountBen,
        "amount": amount
    }
    answer = requests.post("https://api.lava.ru/transfer/create", headers=headers, data=data)
    if answer.json()["status"] == "success":
        return True
    else:
        return answer.json()["message"]


#  Receiving all transfers. Returns to the data array
def TransactionsList(token, account, type=None, limit=None):
    if not CheckWallet(token):
        return "Invalid token"
    headers = {
        "Authorization": token,
    }
    data = {
        "transfer_type": type,
        "account": account,
        "limit": limit
    }
    answer = requests.post("https://api.lava.ru/transactions/list", headers=headers, data=data)
    return answer.json()["items"]


#  Creating an invoice for payment. Returns to String
def InvoiceCreate(token, account, amount, expire=None, successUrl=None,
                  failUrl=None, subtract=0, comment=None, merchantName=None):
    if not CheckWallet(token):
        return "Invalid token"
    headers = {
        "Authorization": token,
    }
    data = {
        "wallet_to": account,
        "sum ": amount,
        "success_url": successUrl,
        "fail_url": failUrl,
        "expire": expire,
        "subtract": subtract,
        "comment": comment,
        "merchant_name": merchantName
    }
    answer = requests.post("https://api.lava.ru/invoice/create", headers=headers, data=data)
    if answer.json()["status"] == "success":
        return answer.json()
    else:
        if answer.json()["message"] == "Invalid token":
            return "You do not have enough rights to create a payment invoice"
        return answer.json()["message"]


#  Information about the created account. Returns to String
def InvoiceInfo(token, id):
    if not CheckWallet(token):
        return "Invalid token"
    headers = {
        "Authorization": token,
    }
    data = {
        "id": id
    }
    answer = requests.post("https://api.lava.ru/invoice/info", headers=headers, data=data)
    if answer.json()["status"] == "success":
        return answer.json()
    else:
        if answer.json()["message"] == "Invalid token":
            return "You do not have enough rights to create a payment invoice"
        return answer.json()["message"]