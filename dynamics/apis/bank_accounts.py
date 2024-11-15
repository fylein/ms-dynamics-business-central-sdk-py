from .api_base import ApiBase


class BankAccounts(ApiBase):
    """Class for Bank Accounts APIs."""

    GET_BANK_ACCOUNT = '/bankAccounts'
    COUNT_BANK_ACCOUNT = '/bankAccounts/$count'

    def get_all(self, **kwargs):
        """
        Get all bank accounts
        :return: returns all bank accounts
        """
        return self._get_request({
            **kwargs
        }, BankAccounts.GET_BANK_ACCOUNT)['value']

    def count(self, **kwargs):
        """
        Get counts of locations
        :return: Count in Int
        """
        return self._get_request_for_count({
            **kwargs
        }, BankAccounts.COUNT_BANK_ACCOUNT)['value']
