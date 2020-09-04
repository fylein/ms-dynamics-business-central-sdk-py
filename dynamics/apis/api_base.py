from dynamics.exceptions import *
import requests
import json


class ApiBase:
    """The base class for all API classes."""

    def __init__(self):
        self.__access_token = None
        self.__server_url = None

    def change_access_token(self, access_token):
        """Change the old access token with the new one.

        Parameters:
            access_token (str): The new access token.
        """
        self.__access_token = access_token

    def set_server_url(self, server_url):
        """Set the server URL dynamically upon creating a connection

        Parameters:
            server_url(str): The current server URL
        """
        self.__server_url = server_url

    def _get_request(self, params, api_url):
        """Create a HTTP GET request.

        Parameters:
            params (dict): HTTP GET parameters for the wanted API.
            api_url (str): Url for the wanted API.

        Returns:
            A response from the request (dict).
        """

        api_headers = {
            'Authorization': self.__access_token,
            'Accept': 'application/json'
        }
        api_params = {}

        for k in params:
            # ignore all unused params
            if not params[k] is None:
                p = params[k]

                # convert boolean to lowercase string
                if isinstance(p, bool):
                    p = str(p).lower()

                api_params[k] = p

        response = requests.get(
            '{0}{1}'.format(self.__server_url, api_url),
            headers=api_headers,
            params=api_params
        )

        if response.status_code == 200 or response.status_code == 201:
            result = json.loads(response.text)
            return result

        elif response.status_code == 400:
            raise WrongParamsError('Some of the parameters are wrong', response.text)

        elif response.status_code == 401:
            raise InvalidTokenError('Invalid token, try to refresh it', response.text)

        elif response.status_code == 403:
            raise NoPrivilegeError('Forbidden, the user has insufficient privilege', response.text)

        elif response.status_code == 404:
            raise NotFoundItemError('Not found item with ID', response.text)

        elif response.status_code == 498:
            raise ExpiredTokenError('Expired token, try to refresh it', response.text)

        elif response.status_code == 500:
            raise InternalServerError('Internal server error', response.text)

        else:
            raise DynamicsError('Error: {0}'.format(response.status_code), response.text)

    def _post_request(self, data, api_url):
        """Create a HTTP post request.

        Parameters:
            data (dict): HTTP POST body data for the wanted API.
            api_url (str): Url for the wanted API.

        Returns:
            A response from the request (dict).
        """

        api_headers = {
            'Authorization': self.__access_token,
            'Accept': 'application/json'
        }
        response = requests.post(
            '{0}{1}'.format(self.__server_url, api_url),
            headers=api_headers,
            json=data
        )
        if response.status_code == 200 or response.status_code == 201:
            result = json.loads(response.text)
            return result

        elif response.status_code == 400:
            raise WrongParamsError('Some of the parameters are wrong', response.text)

        elif response.status_code == 401:
            raise InvalidTokenError('Invalid token, try to refresh it', response.text)

        elif response.status_code == 403:
            raise NoPrivilegeError('Forbidden, the user has insufficient privilege', response.text)

        elif response.status_code == 404:
            raise NotFoundItemError('Not found item with ID', response.text)

        elif response.status_code == 498:
            raise ExpiredTokenError('Expired token, try to refresh it', response.text)

        elif response.status_code == 500:
            raise InternalServerError('Internal server error', response.text)

        else:
            raise DynamicsError('Error: {0}'.format(response.status_code), response.text)

    def _patch_request(self, content_type, data, api_url):
        """Create a HTTP patch request.

        Parameters:
            data: HTTP POST body data for the wanted API.
            api_url (str): Url for the wanted API.

        Returns:
            A response from the request (dict).
        """

        api_headers = {
            'Authorization': self.__access_token,
            'If-Match': '*',
            'Content-Type': content_type
        }
        response = requests.patch(
            '{0}{1}'.format(self.__server_url, api_url),
            headers=api_headers,
            data=data
        )

        if response.status_code == 200 or response.status_code == 201 or response.status_code == 204:
            return

        elif response.status_code == 400:
            raise WrongParamsError('Some of the parameters are wrong', response.text)

        elif response.status_code == 401:
            raise InvalidTokenError('Invalid token, try to refresh it', response.text)

        elif response.status_code == 403:
            raise NoPrivilegeError('Forbidden, the user has insufficient privilege', response.text)

        elif response.status_code == 404:
            raise NotFoundItemError('Not found item with ID', response.text)

        elif response.status_code == 498:
            raise ExpiredTokenError('Expired token, try to refresh it', response.text)

        elif response.status_code == 500:
            raise InternalServerError('Internal server error', response.text)

        else:
            raise DynamicsError('Error: {0}'.format(response.status_code), response.text)