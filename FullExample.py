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

# Payment check every 5 seconds
from time import sleep

while True:
    if payment.is_paid():
        print("Payment is paid!")
        break

    sleep(5)
