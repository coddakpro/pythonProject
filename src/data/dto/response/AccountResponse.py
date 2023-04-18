class AccountResponse:
    def __init__(self):
        self._account_id = ""
        self._first_name = ""
        self._last_name = ""
        self._full_name = ""
        self._mobile_number = ""
        self._age = ""
        self._gender = ""
        self._realship = ""
        self._lga = ""
        self._state = ""
        self._email = ""

    def set_account_id(self, account_id):
        self._account_id = account_id

    def get_account_id(self):
        return self._account_id   

    def set_email(self, email: str) -> None:
        self._email = email

    def get_email(self) -> str:
        return self._email

    def set_state(self, state: str) -> None:
        self._state = state

    def get_state(self) -> str:
        return self._state

    def set_lga(self, lga: str) -> None:
        self._lga = lga

    def get_lga(self) -> str:
        return self._lga

    def set_mobile_number(self, number: str) -> None:
        self._mobile_number = number

    def get_mobile_number(self) -> str:
        return self._mobile_number

    def set_full_name(self, name):
        self._full_name = name

    def get_full_name(self):
        return self._full_name

    def set_first_name(self, first_name) -> None:
        self._first_name = first_name

    def get_first_name(self) -> str:
        return self._first_name

    def set_last_name(self, last_name) -> None:
        self._last_name = last_name

    def get_last_name(self) -> str:
        return self._last_name

    def set_gender(self, gender) -> None:
        self._gender = gender

    def get_gender(self):
        return self._gender

    def __str__(self):
        return f"""
            first_name: {self._first_name},
            last_name: {self._last_name},
            full_name: {self._full_name},
            Gender: {self._gender},
            RelationshipStatus: {self._realship},
            mobile_number: {self._mobile_number},
            local_government: {self._lga},
            state_of_origin: {self._state},
            email_address: {self._email}
        """
    
    def __repr__(self):
        return f"""
            first_name: {self._first_name},
            last_name: {self._last_name},
            full_name: {self._full_name},
            Gender: {self._gender},
            RelationshipStatus: {self._realship},
            mobile_number: {self._mobile_number},
            local_government: {self._lga},
            state_of_origin: {self._state},
            email_address: {self._email}
        """

