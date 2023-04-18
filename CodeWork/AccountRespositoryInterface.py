class AccountRequest:
    def __init__(self, first_name, last_name, mobile_number, age, gender, realship, lga, state, email):
        self._first_name = first_name,
        self._last_name = last_name,
        self._mobile_number = mobile_number,
        self._age = age,
        self._gender = gender
        self._realship = realship
        self._lga = lga
        self._state = state
        self._email = email

    def set_email(self, email: str):
        self._email = email

    def get_email(self):
        return self._email

    def set_state(self, state: str):
        self._state = state

    def get_state(self):
        return self._state

    def set_lga(self, lga: str):
        self._lga = lga

    def get_lga(self):
        return self._lga

    def set_mobile_number(self, number: str):
        self._mobile_number = number

    def get_mobile_number(self):
        return self._mobile_number

    def set_full_name(self, first_name, last_name):
        self._first_name = first_name
        self._last_name = last_name

    def get_full_name(self):
        return '{} {}'.format(self._first_name, self._last_name)

    def set_first_name(self, first_name) -> None:
        self._first_name = first_name

    def get_first_name(self):
        return self._first_name

    def set_last_name(self, last_name):
        self._last_name = last_name

    def get_last_name(self):
        return self._last_name

    def set_gender(self, gender):
        self._gender = gender

    def get_gender(self):
        return self._gender

    def __str__(self):
        return f"""
            first_name: {self._first_name},
            last_name: {self._last_name},
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
            Gender: {self._gender},
            RelationshipStatus: {self._realship},
            mobile_number: {self._mobile_number},
            local_government: {self._lga},
            state_of_origin: {self._state},
            email_address: {self._email}
        """

