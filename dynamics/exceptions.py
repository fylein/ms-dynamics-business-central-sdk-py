"""
Dynamics SDK Exceptions
"""


class DynamicsError(Exception):
    """The base exception class for Dynamics.

    Parameters:
        msg (str): Short description of the error.
        response: Error response from the API call.
    """

    def __init__(self, msg, response=None):
        super(DynamicsError, self).__init__(msg)
        self.message = msg
        self.response = response

    def __str__(self):
        return repr(self.message)


class NotFoundClientError(DynamicsError):
    """Client not found OAuth2 authorization, 404 error."""
    pass


class UnauthorizedClientError(DynamicsError):
    """Wrong client secret and/or refresh token, 401 error."""
    pass


class ExpiredTokenError(DynamicsError):
    """Expired (old) access token, 498 error."""
    pass


class InvalidTokenError(DynamicsError):
    """Wrong/non-existing access token, 401 error."""
    pass


class NoPrivilegeError(DynamicsError):
    """The user has insufficient privilege, 403 error."""
    pass


class WrongParamsError(DynamicsError):
    """Some of the parameters (HTTP params or request body) are wrong, 400 error."""
    pass


class NotFoundItemError(DynamicsError):
    """Not found the item from URL, 404 error."""
    pass
    

class InternalServerError(DynamicsError):
    """The rest Dynamics errors, 500 error."""
    pass
