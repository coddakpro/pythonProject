from data.dto.request.AccountRequest import AccountRequest
from data.dto.response.AccountResponse import AccountResponse
from data.model.Account import Account
from data.model.User import User
from data.model.personal_information import PersonalInformation
from data.repository.AccountRepositoryInterface import AccountRepositoryInterface
import random
from data.model.Gender import Gender


class AccountRepositoryImpl(AccountRepositoryInterface):
    account_data_base = {}
    account_id_count: int = 0
    account = Account()
    personal_info = PersonalInformation()
    user = User()

    def create_new_account(self, account_request: AccountRequest) -> AccountResponse:
        account_response = AccountResponse()

        self.account.set_id(self.account_id_count + 1)
        self.personal_info.set_first_name(account_request.get_first_name())
        self.personal_info.set_last_name(account_request.get_last_name())
        self.personal_info.set_email_address(account_request.get_email())
        self.personal_info.set_mobile_number(account_request.get_mobile_number())
        self.personal_info.set_local_govt(account_request.get_lga())
        self.personal_info.set_state_of_origin(account_request.get_state())
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


if __name__ == '__main__':
    account_request = AccountRequest("Elite", "C15", "90908765432", 234, "She_Him", "Hooked", "Sabo Local Govt",
                                     "Lagos State", "elite@examplemail.com")

    acc_repo_impl = AccountRepositoryImpl()
    account_response: AccountResponse() = acc_repo_impl.create_new_account(account_request)

    value = acc_repo_impl.find_account_by_id(1)
    print(value)
