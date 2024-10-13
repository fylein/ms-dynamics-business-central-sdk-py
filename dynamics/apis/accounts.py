from .api_base import ApiBase


class Accounts(ApiBase):
    """Class for Accounts APIs."""

    GET_ACCOUNTS = '/accounts'
    POST_ACCOUNT = '/accounts'
    COUNT_ACCOUNT = "/accounts/$count"

    def get_all(self, **kwargs):
        """
        Get all accounts
        :return: returns all companies
        """
        return self._get_request({
            **kwargs
        }, Accounts.GET_ACCOUNTS)['value']

    def count(self, **kwargs):
        """
        Get counts of accounts
        :return: Count in Int
        """
        return self._get_request_for_count({
            **kwargs
        }, Accounts.COUNT_ACCOUNT)['value']
    