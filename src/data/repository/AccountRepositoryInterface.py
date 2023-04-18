from abc import ABC, abstractmethod

from data.dto.request.AccountRequest import AccountRequest
from data.dto.response.AccountResponse import AccountResponse


class AccountRepositoryInterface(ABC):
    @abstractmethod
    def create_new_account(self, account_request: AccountRequest) -> AccountResponse:
        pass

    @abstractmethod
    def find_account_by_id(self, id):
        pass

    @abstractmethod
    def find_account_by_account_name(self, name):
        pass

    @abstractmethod
    def delete_account_by_id(self, id):
        pass

    @abstractmethod
    def delete_account_by_account_name(self, name):
        pass

    @abstractmethod
    def update_account_by_id(self, id):
        pass

    @abstractmethod
    def update_account_by_name(self, name):
        pass
    
    
