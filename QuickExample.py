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
