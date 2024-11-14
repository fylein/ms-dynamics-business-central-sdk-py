from .api_base import ApiBase


class Dimensions(ApiBase):
    """Class for Locations APIs."""

    GET_DIMENSION = '/dimensions'
    GET_DIMENSION_VALUES = '/dimensions({0})/dimensionValues'
    COUNT_DIMENSIONS = '/dimensions/$count'
    COUNT_DIMENSIONS_VALUES = '/dimensions({0})/dimensionValues/$count'

    def get_all_dimensions(self, **kwargs):
        """
        Get all dimensions
        :return: returns all companies
        """
        return self._get_request({
            **kwargs
        }, Dimensions.GET_DIMENSION)['value']

    def get_all_dimension_values(self, dimension_id:str, **kwargs):
        """
        Get all dimension_values

        Parameters:
            dimension_name (str): Dimension name.

        :return: returns all companies
        """
        return self._get_request({
            **kwargs
        }, (Dimensions.GET_DIMENSION_VALUES).format(dimension_id))['value']

    def count(self, **kwargs):
        """
        Get counts of dimensions
        :return: Count in Int
        """
        return self._get_request_for_count({
            **kwargs
        }, Dimensions.COUNT_DIMENSIONS)['value']

    def count_dimension_values(self, destination_id:str, **kwargs):
        """
        Get counts of dimensions values with the given destination_id
        :return: Count in Int
        """

        return self._get_request_for_count({
            **kwargs
        }, (Dimensions.COUNT_DIMENSIONS_VALUES).format(destination_id))['value']
