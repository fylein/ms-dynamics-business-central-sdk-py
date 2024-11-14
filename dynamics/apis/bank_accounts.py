from .api_base import ApiBase


class BankAccounts(ApiBase):
    """Class for Bank Accounts APIs."""

    GET_BANK_ACCOUNT = '/bankAccounts'

    def get_all(self, **kwargs):
        """
        Get all bank accounts
        :return: returns all bank accounts
        """
        return self._get_request({
            **kwargs
        }, BankAccounts.GET_BANK_ACCOUNT)['value']
