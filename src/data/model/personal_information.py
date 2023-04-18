from data.model.Country import Country
from data.model.Gender import Gender
from data.model.RelationshipStatus import RelationshipStatus


class PersonalInformation:
    def __init__(self):
        self._person_id: int = 0
        self._first_name: str = ""
        self._last_name: str = ""
        self._gender = Gender
        self._relationship_status = RelationshipStatus
        self._mobile_number: str = ""
        self._country_code = Country
        self._local_government: str = ""
        self._state_of_origin: str = ""
        self._email_address: str = ""

    def set_id(self, person_id):
        self._person_id = person_id

    def get_id(self):
        return self._person_id

    def set_email_address(self, email: str) -> None:
        self._email_address = email

    def get_email_address(self) -> str:
        return self._email_address

    def set_state_of_origin(self, state: str) -> None:
        self._state_of_origin = state

    def get_state_of_origin(self) -> str:
        return self._state_of_origin

    def set_local_govt(self, lga: str) -> None:
        self._local_government = lga

    def get_local_govt(self) -> str:
        return self._local_government

    def set_mobile_number(self, number: str) -> None:
        self._mobile_number = number

    def get_mobile_number(self) -> str:
        return self._mobile_number

    def set_country_code(self, code) -> None:
        self._country_code = code

    def get_country_code(self):
        return self._country_code

    def set_full_name(self, first_name, last_name):
        self._first_name = first_name
        self._last_name = last_name

    def get_full_name(self):
        return '{} {}'.format(self._first_name, self._last_name)

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
            person_id: {self._person_id},
            first_name: {self._first_name},
            last_name: {self._last_name},
            Gender: {self._gender},
            RelationshipStatus: {self._relationship_status},
            mobile_number: {self._mobile_number},
            Country: {self._country_code},
            local_government: {self._local_government},
            state_of_origin: {self._state_of_origin},
            email_address: {self._email_address}
        """
    
    def __repr__(self):
        return f"""
            person_id: {self._person_id},
            first_name: {self._first_name},
            last_name: {self._last_name},
            Gender: {self._gender},
            RelationshipStatus: {self._relationship_status},
            mobile_number: {self._mobile_number},
            Country: {self._country_code},
            local_government: {self._local_government},
            state_of_origin: {self._state_of_origin},
            email_address: {self._email_address}
        """
