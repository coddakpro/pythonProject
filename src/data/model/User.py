from data.model.NextOfKin import NextOfKin
from data.model.Address import Address
from data.model.personal_information import PersonalInformation


class User:
    def __init__(self):
        self._next_of_kin = NextOfKin()
        self._user_address = Address()
        self._user_personal_information = PersonalInformation()

    def set_personal_info(self, personal_info):
        self._user_personal_information = personal_info

    def get_personal_info(self):
        return self._user_personal_information

    def __str__(self):
        return f"""
            NextOfKin: {self._next_of_kin}, 
            Address: {self._user_address}, 
            PersonalInformation: {self._user_personal_information}
        """

    def __repr__(self):
        return f"""
            NextOfKin: {self._next_of_kin}, 
            Address: {self._user_address}, 
            PersonalInformation: {self._user_personal_information}
        """

