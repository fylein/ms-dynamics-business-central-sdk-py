from .api_base import ApiBase


class Employees(ApiBase):
    """Class for Employees APIs."""

    GET_EMPLOYEES = '/employees'
    POST_EMPLOYEES = '/employees'
    COUNT_EMPLOYEES = '/employees/$count'

    def get_all(self, **kwargs):
        """
        Get all employees
        :return: returns all employees
        """
        return self._get_request({
            **kwargs
        }, Employees.GET_EMPLOYEES)['value']
    
    def post(self, data):
        """
        Create Employee
        :param data:
        :return:
        """
        return self._post_request(data, Employees.POST_EMPLOYEES)

    def count(self, **kwargs):
        """
        Get counts of employees
        :return: Count in Int
        """
        return self._get_request_for_count({
            **kwargs
        }, Employees.COUNT_EMPLOYEES)['value']
