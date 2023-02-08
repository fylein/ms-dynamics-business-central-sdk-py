from .api_base import ApiBase


class ItemsByLocation(ApiBase):
    """Class for ItemsByLocation APIs."""

    GET_ItemsByLocation = '/ItemsByLocation'
    POST_VENDOR = '/ItemsByLocation'

    def get(self, **kwargs):
        """
        Get all ItemsByLocation
        :return: returns all companies
        """
        return self._get_request({
            **kwargs
        }, ItemsByLocation.GET_ItemsByLocation)['value']

   
