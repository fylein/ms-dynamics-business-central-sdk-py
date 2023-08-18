from .api_base import ApiBase


class Accounts(ApiBase):
    """Class for Accounts APIs."""

    GET_ACCOUNTS = '/accounts'
    POST_ACCOUNT = '/accounts'

    def get_all(self, **kwargs):
        """
        Get all accounts
        :return: returns all companies
        """
        return self._get_request({
            **kwargs
        }, Accounts.GET_ACCOUNTS)['value']
