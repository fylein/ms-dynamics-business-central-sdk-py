from .api_base import ApiBase


class Dimensions(ApiBase):
    """Class for Locations APIs."""

    GET_DIMENSION = '/dimensions'
    GET_DIMENSION_VALUES = '/dimensions({0})/dimensionValues'

    def get_all_dimensions(self, **kwargs):
        """
        Get all dimensions
        :return: returns all companies
        """
        return self._get_request({
            **kwargs
        }, Dimensions.GET_DIMENSION)['value']

    def get_all_dimension_values(self, dimension_name:str, **kwargs):
        """
        Get all dimension_values

        Parameters:
            dimension_name (str): Dimension name.

        :return: returns all companies
        """
        return self._get_request({
            **kwargs
        }, (Dimensions.GET_DIMENSION_VALUES).format(dimension_name))['value']
