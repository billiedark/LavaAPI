[![N|Solid](https://github.com/billiedark/LavaAPI/blob/main/LavaAPI.png?raw=true)](https://pypi.org/project/lavaapi/)

![Python](https://img.shields.io/badge/-Python-0a0a0a?style=for-the-badge&logo=python&logoColor=24e387)

This library was created to simplify the LAVA api [provided on the official website](https://dev.lava.ru/), in the Python programming language.  
Эта библиотека создана для упрощения работы с LAVA api, [предоставленной на официальном сайте](https://dev.lava.ru/), на языке программирования Python.


## Features - Возможности

- Checking token validity - Проверка токена на валидность
- Detailed validity check of the token - Подробная проверка токена на валидность
- Checking wallet balance - Проверка баланса кошелька
- Withdrawal from a wallet - Вывод из кошелька
- Transfers between wallets - Переводы между кошельками
- Transfer history of your wallet - История переводов вашего кошелька
- Creating a bill for payment - Создания счета для оплаты
- Information about the bill - Информация о созданном счете

  
## Installation - Установка

[Python](https://www.python.org/) version 3.6 or higher must be installed  
Необходимо установить [Python](https://www.python.org/) версии не ниже 3.6

```cmd
pip install requests
pip install lavaapi
```
  
## Using - Использование
To get your TOKEN, you need to register in LAVA and get your key [by following this link](https://lava.ru/settings/api)  
Для получения вашего ТОКЕНА необходимо зарегистрироваться в LAVA и получить свой ключ [по этой ссылке](https://lava.ru/settings/api)  
  
API key = Token
  
### Checking token validity - Проверка токена на валидность
Returns True or False  
Возвращает True или False
```python
CheckWallet("YOUR_TOKEN")
```
  
### Detailed validity check of the token - Подробная проверка токена на валидность
Returns True if valid or String with error  
Возвращает True если валидный или String с ошибкой, если токен невалидный
```python
CheckWalletDetails("YOUR_TOKEN")
```
  
### Checking wallet balance - Проверка баланса кошелька
Returns String  
Возвращает String  
  
CURRENCY: "USD", "EUR" or "RUB"
```python
WalletBalance("YOUR_TOKEN", "CURRENCY")
```
  
### Withdrawal from a wallet - Вывод из кошелька
Returns True or String with error 
Возвращает True или String с ошибкой  
  
ACCOUNT_ID: Your account number (For example: R10007689)  
AMOUNT: Withdrawal amount in Int  
SERVICE: "qiwi", "yoomoney", "card", "advcash", "payeer", "mobile", "perfect"  
WALLET_TO: Wallet, where the money will be withdrawn  
```python
WithdrawCreate("YOUR_TOKEN", "ACCOUNT_ID", AMOUNT, "SERVICE", "WALLET_TO")
```
  
Example:
```python
WithdrawCreate("MY_TOKEN", "R10007689", 100, "qiwi", "88005553535")
```
  
### Transfers between wallets - Переводы между кошельками
Returns True or String with error  
Возвращает True или String с ошибкой  
  
ACCOUNT_ID: Your account number (For example: R10007689)  
AMOUNT: Transferable amount in Int  
ACCOUNT_TO: Account to which the money will be transferred  
```python
TransferCreate("YOUR_TOKEN", "ACCOUNT_ID", AMOUNT, "ACCOUNT_TO")
```
  
Example:
```python
TransferCreate("MY_TOKEN", "R10007689", 500, "R100126592")
```
  
### Transfer history of your wallet - История переводов вашего кошелька
Returns an array of data  
Возвращает массив данных  
  
ACCOUNT_ID: Your account number (For example: R10007689)  
**TYPE: "withdraw" or "transfer"  
**LIMIT: Number of records that will be returned  
  
** - Optional parameter - Необязательный параметр
```python
TransactionsList("YOUR_TOKEN", "ACCOUNT_ID", type="TRANSLATION_TYPE", limit=MAX_TRANSLATION)
```
  
Example:
```python
myTranslations = TransactionsList("MY_TOKEN", "R10007689", limit=3)
print(myTranslations[0]["amount"], myTranslations[0]["comment"])
```
```cmd
1230.00 Hello
```
  
Full function output:
```java
[
    {
        "id": "bc81edeb-3f81-156d-21bd-06c67010094f", // Номер транзакции
        "created_at": "1634902579",  // Время создания (unix timestamp)
        "created_date": "2021-10-22T11:36:19+00:00", // Время создания
        "amount": "1230.00", // Сумма транзакции
        "status": "success", // Статус транзакции
        "transfer_type": "transfer", // Тип перевода
        "comment": "Hello", // Комментарий
        "method": "-1", // Метод 1 - зачисление, -1 - расход
        "currency": "RUB", // Валюта
        "account": "R10000001", // Номер аккаунта
        "commission": "12.30", // Комиссия
        "type": "out", // Тип in - пополнение, out - перевод
        "receiver": "R10000000" // Номер аккаунта получателя
    },
    {
        "id": "3e22b0c8-2c4a-93d8-2f6d-b93ce824ee62",
        "created_at": "1634899536",
        "created_date": "2021-10-22T10:45:36+00:00",
        "amount": "1000.01",
        "commission": "0.00",
        "status": "pending",
        "transfer_type": "withdraw",
        "service": "card",
        "comment": null,
        "method": "-1",
        "currency": "RUB",
        "account": "R10000001"
    },
    {
        "id": "f569a6e7-14e4-1895-374c-c9dd6775c0ce",
        "created_at": "1634744391",
        "created_date": "2021-10-20T15:39:51+00:00",
        "amount": "1000.00",
        "status": "pending",
        "transfer_type": "transfer",
        "comment": "123123",
        "method": "1",
        "currency": "RUB",
        "account": "R10000001",
        "commission": 0,
        "type": "in",
        "sender": "system" // Отправитель
    },
]
```
  
### Creating a bill for payment - Создания счета для оплаты
Returns Json array  
Возвращает массив Json  
  
ACCOUNT_ID: Your account number (For example: R10007689)  
AMOUNT: Transferable amount in Int  
**EXPIRE: The time in minutes after which the account will automatically close. By standard 1440  
**SUCCESSURL: Url for redirection after successful payment  
**FAILURL: Url for redirecting after unsuccessful payment  
**SUBTRACT: Who to charge the commission to (1 - Write off from the client, 0 - Write off from the store). By standard 0  
**COMMENT: Payment comment  
**MERCHANTNAME: Merchant name (displayed in the translation form)  
  
** - Optional parameter - Необязательный параметр
```python
InvoiceCreate("YOUR_TOKEN", "ACCOUNT_ID", AMOUNT, expire=None, successUrl=None,
                  failUrl=None, subtract=0, comment=None, merchantName=None)
```
  
Example:
```python
billCreate = InvoiceCreate("MY_TOKEN", "R10007689", 150, comment="DBD20RANK")
print("Payment link:", billCreate["url"])
```
```text
Payment link: https://p2p.lava.ru/form?id=1ee31634-e3e0-34ce-1423-b5b4cb524c6a
```
  
Full function output:
```java
{
    "status": "success",
    // Номер счета на оплату
    "id": "1ee31634-e3e0-34ce-1423-b5b4cb524c6a",
    // Ссылка на оплату
    "url": "https://p2p.lava.ru/form?id=1ee31634-e3e0-34ce-1423-b5b4cb524c6a",
    // Время истечения счета
    "expire": 1636983503,
    // Сумма счета
    "sum": "100.00",
    // URL для переадресации после успешной оплаты 
    "success_url": "https://lava.ru?success",
    // URL для переадресации после неудачной оплаты 
    "fail_url": "https://lava.ru?fail",
    // URL для отправки webhook
    "hook_url": "https://lava.ru?hook",
    // Дополнительное поле
    "custom_fields": "123",
    // ID и наименование мерчанта
    "merchant_name": "123",
    "merchant_id": "123",
}
```

### Information about the bill - Информация о созданном счете
Returns Json array  
Возвращает массив Json  
  
ACCOUNT_ID: Your account number (For example: R10007689)  
BILL_ID: Billed number

```python
InvoiceInfo("YOUR_TOKEN", "BILL_ID")
```
  
Example:
```python
billCreate = InvoiceInfo("MY_TOKEN", "R10007689", "1ee31634-e3e0-34ce-1423-b5b4cb524c6a")
print(billCreate["invoice"]["comment"])
```
```text
На бигтести с колой
```
  
Full function output:
```java
{
    "status": "success",
    "invoice": {
        // Номер счета на оплату
        "id": "1ee31634-e3e0-34ce-1423-b5b4cb524c6a",
        // Номер счета в системе клиента
        "order_id": "order_125",
        // Время истечение счета
        "expire": 1636983503,
        // Сумма счета
        "sum": "100.00",
        // Комментарий
        "comment": "На бигтести с колой",
        // Статус счета
        "status": "success",
        // URL для переадресации после успешной оплаты 
        "success_url": "https://lava.ru?success",
        // URL для переадресации после неудачной оплаты 
        "fail_url": "https://lava.ru?fail",
        // URL для отправки webhook
        "hook_url": "https://lava.ru?hook",
        // Дополнительное поле
        "custom_fields": "123"
    }
}
```

Скоро в библиотеку будут добавлены более простые методы
  
## License
  
MIT
