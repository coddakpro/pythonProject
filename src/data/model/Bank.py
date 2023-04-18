from _ast import Return

from data.model.Address import Address


class Bank:
    def __init__(self):
        self._bank_id: int = 0
        self._bank_name: str = ""
        self._bank_branch_location = Address()
        self._branch_sort_code: int = 0
        self._bank_swift_code: int = 0
        self._bank_manager: str = ""
        self._account_id_list: list = []

        def set_account_id(self, account_id):
            self._account_id_list.append(account_id)

            def get_account_id(self):
                return self._bank_id


    def set_bank_name(self, bank_name):
        self._bank_name = bank_name

    def get_bank_name(self):
        return self._bank_name

    def set_bank_id(self, bank_id):
        self._bank_id = bank_id

    def get_bank_id(self):
        return self._bank_id

    def set_bank_branch_location(self, bank_branch_location):
        self._bank_branch_location = bank_branch_location

    def get_bank_branch_location(self):
        return self._bank_branch_location

    def set_branch_sort_code(self, branch_sort_code) -> None:
        self._branch_sort_code = branch_sort_code

    def set_bank_swift_code(self, bank_swift_code) -> None:
        self._bank_swift_code = bank_swift_code

    def get_bank_swift_code(self):
        return self._bank_swift_code

    def set_bank_manager(self, acc_number: str) -> None:
        self._bank_manager = acc_number

    def get_bank_manager(self):
        return self._bank_manager

    def __repr__(self):
        return f"""Bank Id: {self._bank_id}, 
                      Branch Sort Code: {self._branch_sort_code} , 
                      Bank Swift Code: {self._bank_swift_code}, 
                      Bank Name: {self._bank_name}, 
                      Bank Manager: {self._bank_manager},
                      Bank Branch Location: {self._bank_branch_location}
                  """

    def __str__(self):
        return f"""Bank Id: {self._bank_id}, 
              Branch Sort Code: {self._branch_sort_code} , 
              Bank Swift Code: {self._bank_swift_code}, 
              Bank Name: {self._bank_name},
              Bank Manager: {self._bank_manager},
              Bank Branch Location: {self._bank_branch_location}
          """
