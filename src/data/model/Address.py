from data.model.State import State
from data.model.Country import Country


class Address:

    def __init__(self):
        self._address_id: int = 0
        self._street_name: str = ""
        self._street_number: str = ""
        self._postal_code: int = 0
        self._local_government: str = ""
        self._state = State
        self._country = Country

    def set_street_name(self, street_name: str):
        self._street_name = street_name

    def get_street_name(self):
        return self._street_name

    def set_street_number(self, street_number: str):
        self._street_number = street_number

    def get_street_number(self):
        return self._street_number

    def set_address_id(self, address_id: int):
        self._address_id = address_id

    def get_address_id(self):
        return self._address_id

    def set_postal_code(self, postal_code: int):
        self._postal_code = postal_code

    def get_postal_code(self):
        return self._postal_code

    def set_local_government(self, local_government: str) -> None:
        self._local_government = local_government

    def get_local_government(self):
        return self._local_government

    def set_state(self, state: State) -> None:
        self._state = state

    def get_state(self):
        return self._state

    def set_country(self, country: Country) -> None:
        self._country = country

    def get_country(self):
        return self._country

    def __repr__(self):
        return f"""
                    Address Id: {self._address_id},
                    Local Goverment: {self._local_government},
                    Street Number: {self._street_number},
                    Street Name: {self._street_name},
                    State: {self._state},
                    Postal Code: {self._postal_code},
                    Country: {self._country}
                """


