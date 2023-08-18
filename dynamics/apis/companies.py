from .api_base import ApiBase


class Companies(ApiBase):
    """Class for Companies APIs."""

    GET_COMPANIES = '/companies'

    def get_all(self, **kwargs):
        """
        Get all companies
        :return: returns all companies
        """
        return self._get_request({
            **kwargs
        }, Companies.GET_COMPANIES)['value']
