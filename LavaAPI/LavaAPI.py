from __future__ import annotations
from requests import get, post


class Payment:

    def __init__(self, payment_id: str, headers: dict, url: str, api_url: str, amount: int) -> Payment:
        self.id = payment_id
        self.headers = headers
        self.url = url  # Taking the full link in case of changes in the API
        self.amount = amount
        self.api_url = api_url + '/invoice/info'

    def is_paid(self) -> bool:
        data = {"id": self.id}
        if post(self.api_url, headers=self.headers, data=data).json()["invoice"]["status"] == "success":
            return True
        else:
            return False


class LavaAPI(object):

    def __init__(self, key: str) -> LavaAPI:
        """
        Token from lava.ru/dashboard/settings/api
        :param key:
        """
        self.token = key
        self.headers = {"Authorization": key}
        self.url = "https://api.lava.ru"

        self.check_key()

    def check_key(self) -> bool:
        if not get(self.url + "/test/ping", headers=self.headers).json()["status"]:
            raise AuthError("Неверный ключ API (Invalid API key)")
        return True

    def currency_convert(self, currency: str) -> int:
        if currency not in ["USD", "EUR", "RUB"]:
            raise AuthError("Invalid currency")

        if currency == "RUB":
            return 0
        elif currency == "USD":
            return 1
        else:
            return 2

    def wallet_details(self) -> dict:
        return get(self.url + "/wallet/list", headers=self.headers).json()

    def wallet_balance(self, currency: str) -> float:
        """
        USD, EUR, RUB
        :param currency:
        :return:
        """

        return self.wallet_details()[self.currency_convert(currency)]["balance"]

    def create_invoice(self, amount: float, comment: str) -> Payment:
        """
        Only RUB currency
        :param amount:
        :param comment:
        :return:
        """
        data = {
            "wallet_to": self.wallet_details()[0]["account"],
            "sum": amount,
            "comment": comment
        }
        data = post(self.url + "/invoice/create", headers=self.headers, data=data).json()
        if data["status"] != "success":
            raise CreateInvoiceError(data["message"])

        return Payment(data["id"], self.headers, data["url"], self.url, data["sum"])


class AuthError(Exception):
    pass


class CreateInvoiceError(Exception):
    pass
