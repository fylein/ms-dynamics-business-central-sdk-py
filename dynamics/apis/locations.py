from .api_base import ApiBase


class Locations(ApiBase):
    """Class for Locations APIs."""

    GET_LOCATIONS = '/locations'
    POST_LOCATIONS = '/locations'

    def get_all(self, **kwargs):
        """
        Get all locations
        :return: returns all companies
        """
        return self._get_request({
            **kwargs
        }, Locations.GET_LOCATIONS)['value']
