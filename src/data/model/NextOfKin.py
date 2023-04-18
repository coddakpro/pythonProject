from data.model.Address import Address
from data.model.NextOfKinRelationship import NextOfKinRelationship
from data.model.personal_information import PersonalInformation


class NextOfKin:
    def __init__(self):
        self._next_of_kin_address = Address()
        self._next_of_kin_relationship = NextOfKinRelationship
        self._next_of_kin_personal_info = PersonalInformation()

