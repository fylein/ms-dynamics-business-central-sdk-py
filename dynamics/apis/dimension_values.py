from .api_base import ApiBase


class DimensionValues(ApiBase):
    """Class for Locations APIs."""

    GET_DIMENSION_VALUES = '/dimensions({0})/dimensionValues'

    def get_all(self, dimension_name:str, **kwargs):
        """
        Get all dimension_values

        Parameters:
            dimension_name (str): Dimension name.

        :return: returns all companies
        """
        return self._get_request({
            **kwargs
        }, (DimensionValues.GET_DIMENSION_VALUES).format(dimension_name))['value']
