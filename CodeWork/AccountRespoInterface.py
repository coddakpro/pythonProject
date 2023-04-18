import random

from AccountRespositoryInterface import AccountRequest


class AccountRepositoryInterface:
    pass


class Account:
    def set_user(self, user):
        pass

    def set_id(self, param):
        pass

    def set_account_number(self, param):
        pass

    def set_account_name(self, param):
        pass

    def get_id(self):
        pass


class PersonalInformation:
    def set_mobile_number(self, set_mobile_number):
        pass

    def set_first_name(self, set_first_name):
        pass

    def set_last_name(self, set_last_name):
        pass

    def set_email_address(self, set_email):
        pass

    def set_local_govt(self, set_lga):
        pass

    def set_state_of_origin(self, set_state):
        pass

    def get_gender(self):
        pass

    def get_local_govt(self):
        pass

    def get_email_address(self):
        pass

    def get_mobile_number(self):
        pass

    def get_state_of_origin(self):
        pass

    def get_full_name(self):
        pass


class User:
    def set_personal_info(self, personal_info):
        pass

    def get_personal_info(self):
        pass


class Gender:
    FEMALE = None


class AccountResponse:
    pass


class AccountRepositoryImpl(AccountRepositoryInterface):
    account_data_base = {}
    account_id_count: int = 0
    account = Account()
    personal_info = PersonalInformation()
    user = User()

    def create_new_account(self, account_request: AccountRequest) -> AccountResponse:
        account_response = AccountResponse()

        self.account.set_id(self.account_id_count + 1)
        self.personal_info.set_first_name(account_request.set_first_name)
        self.personal_info.set_last_name(account_request.set_last_name)
        self.personal_info.set_email_address(account_request.set_email)
        self.personal_info.set_mobile_number(account_request.set_mobile_number)
        self.personal_info.set_local_govt(account_request.set_lga)
        self.personal_info.set_state_of_origin(account_request.set_state)
        self.user.set_personal_info(self.personal_info)
        self.user.get_personal_info().set_gender(Gender.FEMALE)
        self.user.get_personal_info().get_gender()
        self.account.set_user(self.user)
        self.account.set_account_name(self.user.get_personal_info().get_full_name())
        self.account.set_account_number(self.account_number_generator())

        account_response.set_account_id(self.account.get_id())
        account_response.set_full_name(self.personal_info.get_full_name())
        account_response.set_gender(self.personal_info.get_gender())
        account_response.set_email(self.personal_info.get_email_address())
        account_response.set_mobile_number(self.personal_info.get_mobile_number())
        account_response.set_state(self.personal_info.get_state_of_origin())
        account_response.set_lga(self.personal_info.get_local_govt())

        self.account_data_base[account_response.get_account_id()] = account_response
        return account_response

    @staticmethod
    def account_number_generator():
        value = [str(random.randint(0, 9)) for _ in range(8)]
        str_value = "02"
        for i in value:
            str_value = str_value + i
        return str_value

    def find_account_by_id(self, id):
        return self.account_data_base.get(id)

    def find_account_by_account_name(self, name):
        pass

    def delete_account_by_id(self, id):
        pass

    def delete_account_by_account_name(self, name):
        pass

    def update_account_by_id(self, id):
        pass

    def update_account_by_name(self, name):
        pass


class AccountResponse:
    def set_lga(self, param):
        pass

    def get_account_id(self):
        pass

    def set_state(self, param):
        pass

    def set_mobile_number(self, param):
        pass


if __name__ == '__main__':
    account_request = AccountRequest("Elite", "C15", "90908765432", 234, "She_Him", "Hooked", "Sabo Local Govt",
                                     "Lagos State", "elite@examplemail.com")

    acc_repo_impl = AccountRepositoryImpl()
    account_response: AccountResponse() = acc_repo_impl.create_new_account(account_request)

    value = acc_repo_impl.find_account_by_id(1)
    print(value)