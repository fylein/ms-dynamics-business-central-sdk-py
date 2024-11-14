from .api_base import ApiBase


class Dimensions(ApiBase):
    """Class for Locations APIs."""

    GET_DIMENSION = '/dimensions'

    def get_all(self, **kwargs):
        """
        Get all dimensions
        :return: returns all companies
        """
        return self._get_request({
            **kwargs
        }, Dimensions.GET_DIMENSION)['value']
