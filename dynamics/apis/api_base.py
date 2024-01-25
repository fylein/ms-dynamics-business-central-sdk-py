from dynamics.exceptions.dynamics_exceptions import (
    DynamicsError,
    ExpiredTokenError,
    InvalidTokenError,
    NoPrivilegeError,
    WrongParamsError,
    NotFoundItemError,
    InternalServerError
)
import requests
import json


class ApiBase:
    """The base class for all API classes."""

    def __init__(self):
        self.__access_token = None
        self.__server_url = None
        self.__batch_url = None

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

    def set_batch_url(self, batch_url):
        """Set the batch URL dynamically upon creating a connection

        Parameters:
            batch_url(str): The current batch URL
        """
        self.__batch_url = batch_url

    def _get_request(self, params, api_url):
        """Create a HTTP GET request.

        Parameters:
            params (dict): HTTP GET parameters for the wanted API.

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
            return {'status': 'success'}

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
    
    def _delete_request(self, params, api_url):
        """
        
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

        response = requests.delete(
            '{0}{1}'.format(self.__server_url, api_url),
            headers=api_headers,
            params=api_params
        )

        if response.status_code == 204:
            return {'status': 'success'}

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

    def _bulk_post_request(self, data, isolation: str, company_id: str = None, purchase_invoice_id: str = None):
        """Create a HTTP batch request.

        Parameters:
            data (dict): HTTP POST body data for the wanted API.
            isolation: The isolation level for the batch request.

        Returns:
            A response from the request (dict).
        """
        if company_id:
            self.__batch_url = f'{self.__batch_url}?company={company_id}'

        api_headers = {
            'Authorization': self.__access_token,
            'Accept': 'application/json',
            'Isolation': isolation
        }

        response = requests.post(
            '{0}'.format(self.__batch_url),
            headers=api_headers,
            json=data
        )

        if response.status_code == 200 or response.status_code == 201:
            result = json.loads(response.text)

            error_messages = [resp.get('body', {}).get('error', {}).get('message', None) for resp in result.get('responses', []) if 400 <= resp.get('status', 0) < 500]
            error_messages = [message for message in error_messages if message is not None]

            if error_messages:
                if purchase_invoice_id: self._delete_request({}, '/purchaseInvoices({0})'.format(purchase_invoice_id))
                raise WrongParamsError('Some of the parameters are wrong', error_messages)
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
