from enum import Enum


class Gender(int, Enum):
    MALE = 1
    FEMALE = 2
    OTHERS = 3


for i in Gender:
    print(i)

    # def __str__(self):
    #     return f"""
    #        Male: {self.MALE.value}
    #         Female: {self.FEMALE}
    #         Other: {self.OTHERS}
    #     """
    #
    # def __repr__(self):
    #     return f"""
    #         {self.MALE}
    #         {self.FEMALE}
    #         {self.OTHERS}
    #     """
