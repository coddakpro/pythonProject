from data.model.AccountType import AccountType
from data.model.Bank import Bank
from data.model.User import User


class Account(object):
    def __init__(self):
        self._account_id: int = 0
        self._account_name: str = ""
        self._pin = None
        self._card_number = None
        self._account_type = AccountType
        self._account_number = None
        self._account_user = User()
        self._transfer_limit = None
        self._account_limit = None

    def set_account_name(self, account_name):
        self._account_name = account_name

    def get_account_name(self):
        return self._account_name

    def set_user(self, user):
        self._account_user = user

    def get_user(self):
        return self._account_user

    def set_account_type(self, account_type):
        self._account_type = account_type

    def get_account_type(self):
        return self._account_type

    def set_id(self, account_id):
        self._account_id = account_id

    def get_id(self):
        return self._account_id

    def set_transfer_limit(self, transfer_limit):
        self._transfer_limit = transfer_limit

    def get_transfer_limit(self):
        return self._transfer_limit

    def set_pin(self, pin) -> None:
        self._pin = pin

    def set_card_number(self, card_number) -> None:
        self._card_number = card_number

    def get_card_number(self):
        return self._card_number

    def set_account_number(self, acc_number: str) -> None:
        self._account_number = acc_number

    def get_account_number(self):
        return self._account_number

    def set_account_limit(self, account_limit) -> None:
        self._account_limit = account_limit

    def get_account_limit(self):
        return self._account_limit

    def __repr__(self):
        return f"""User Account Id: {self._account_id},
                    User Account Name: {self._account_name},
                    User Account Pin: {self._pin} ,
                    User Card: {self._card_number},
                    User Bank: {self._bank},
                    User AccountType: {self._account_type},
                    User Account Number: {self._account_number},
                    Account User: {self._account_user},
                    User Transfer Limit: {self._transfer_limit},
                    User account_limit: {self._account_limit}
                """
