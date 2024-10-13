from .api_base import ApiBase


class Locations(ApiBase):
    """Class for Locations APIs."""

    GET_LOCATIONS = '/locations'
    POST_LOCATIONS = '/locations'
    COUNT_LOCATIONS = '/locations/$count'

    def get_all(self, **kwargs):
        """
        Get all locations
        :return: returns all companies
        """
        return self._get_request({
            **kwargs
        }, Locations.GET_LOCATIONS)['value']

    def count(self, **kwargs):
        """
        Get counts of locations
        :return: Count in Int
        """
        return self._get_request_for_count({
            **kwargs
        }, Locations.COUNT_LOCATIONS)['value']
