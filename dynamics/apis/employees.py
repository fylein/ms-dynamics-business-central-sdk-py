from .api_base import ApiBase


class Employees(ApiBase):
    """Class for Employees APIs."""

    GET_EMPLOYEES = '/employees'
    POST_EMPLOYEES = '/employees'

    def get_all(self, **kwargs):
        """
        Get all employees
        :return: returns all employees
        """
        return self._get_request({
            **kwargs
        }, Employees.GET_EMPLOYEES)['value']
