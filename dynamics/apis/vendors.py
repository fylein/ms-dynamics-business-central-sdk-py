from .api_base import ApiBase


class Vendors(ApiBase):
    """Class for Vendors APIs."""

    GET_VENDORS = '/vendors'
    POST_VENDOR = '/vendors'

    def get_all(self, **kwargs):
        """
        Get all vendors
        :return: returns all companies
        """
        return self._get_request({
            **kwargs
        }, Vendors.GET_VENDORS)['value']

    def post(self, data):
        """
        Create Vendor
        :param data:
        :return:
        """
        return self._post_request(data, Vendors.POST_VENDOR)
