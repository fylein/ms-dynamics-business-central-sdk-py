from .api_base import ApiBase


class Environments(ApiBase):
    """Class for environments APIs."""

    GET_ENVIRONMENTS = '/environments/v1.1'

    def get_all(self, **kwargs):
        """
        Get all environments
        :return: returns all environments
        """
        return self._get_request({
            **kwargs
        }, Environments.GET_ENVIRONMENTS)
