from enum import Enum


class Country(Enum):
    NIGERIA = "234"
    GHANA = "233"
    GERMANY = "49"
    GEORGIA = "995"
    SOUTH_AFRICA = "27"
    FRANCE = "33"
    FINLAND = "358"
    ITALY = "39"

    def __repr__(self):
        return f"""
            {self.NIGERIA}
            {self.GHANA}
            {self.GERMANY}
            {self.GEORGIA}
            {self.SOUTH_AFRICA}
            {self.FRANCE}
            {self.FINLAND}
            {self.ITALY}
        """
