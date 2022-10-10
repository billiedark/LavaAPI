[![N|Solid](https://github.com/billiedark/LavaAPI/blob/main/LavaAPI_v2.png?raw=true)](https://nodesource.com/products/nsolid)

![Python](https://img.shields.io/badge/-Python-0a0a0a?style=for-the-badge&logo=python&logoColor=24e387)
  
[![Stargazers repo roster for @billiedark/LavaAPI](https://reporoster.com/stars/billiedark/LavaAPI)](https://github.com/billiedark/LavaAPI/stargazers)  
This library was created to simplify the LAVA api [provided on the official website](https://dev.lava.ru/), in the Python programming language.  
Эта библиотека создана для упрощения работы с LAVA api, [предоставленной на официальном сайте](https://dev.lava.ru/), на языке программирования Python.

  
## Features - Возможности

- Checking token validity - Проверка токена на валидность
- Wallet Details - Подробности кошельков
- Checking wallet balance - Проверка баланса кошелька
- Creating a bill for payment - Создания счета для оплаты
- Information about the bill - Информация о созданном счете


## Installation - Установка

[Python](https://www.python.org/) version 3.6 or higher must be installed  
Необходимо установить [Python](https://www.python.org/) версии не ниже 3.6

```cmd
pip install LavaAPI
```

## Using - Использование
To get your TOKEN, you need to register in LAVA and get your key [by following this link](https://lava.ru/dashboard/settings/api)  
Для получения вашего ТОКЕНА необходимо зарегистрироваться в LAVA и получить свой ключ [по этой ссылке](https://lava.ru/dashboard/settings/api)

Для ясности:  
API key = Token

### Quick example of account creation and payment verification - Быстрый пример создания счета и проверки платежа
Каждые 5 секунд код будет проверять платеж
``` python
from LavaAPI import LavaAPI
from time import sleep

api_key = "YOUR_API_KEY"
api = LavaAPI(api_key)

payment = api.create_invoice(1, "test comment")
print(payment.url)

while True:
    if payment.is_paid():
        print("Payment is paid!")
        break
        
    sleep(5)
```

### Full usage list - Полный список использования
Все примеры с комментариями
```python
from LavaAPI import LavaAPI

api_key = "YOUR_API_KEY"
api = LavaAPI(api_key)

# Get RUB wallet balance
print(api.wallet_balance("RUB"))

# Get EUR wallet balance
print(api.wallet_balance("EUR"))

# Get USD wallet balance
print(api.wallet_balance("USD"))

# Create invoice
payment = api.create_invoice(1, "test")

# Get payment url
print(payment.url)

# Get the invoice amount
print(payment.amount)

# Check payment status
print(payment.is_paid())
```


## License

GNU General Public License (GPL)
