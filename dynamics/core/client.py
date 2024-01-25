import json
import requests
from dynamics.apis import *
from dynamics.exceptions.dynamics_exceptions import *

class Dynamics:
    """
    The main class for connecting to Dynamics APIs.
    """

    TOKEN_URL = 'https://login.microsoftonline.com/organizations/oauth2/v2.0/token?resource=https://api.businesscentral.dynamics.com'
    BASE_URL = 'https://api.businesscentral.dynamics.com/v2.0/{environment}/api/v2.0'

    def __init__(
            self,
            client_id: str,
            client_secret: str,
            environment: str,
            refresh_token: str,
            company_id: str = None
        ):
        """
        Constructor to initialize the Dynamics SDK.
        :param client_id: Dynamics Client ID
        :param client_secret: Dynamics Client Secret
        :param tenant_domain: Dynamics Tenant Domain
        :param environment: Sandbox / Production
        :param refresh_token: Refresh token for authentication
        """
        self.__client_id = client_id
        self.__client_secret = client_secret
        self.__environment = environment
        self.__refresh_token = refresh_token
        self.__company_id = company_id

        # Initialize API instances
        self.companies = Companies()
        self.vendors = Vendors()
        self.accounts = Accounts()
        self.purchase_invoices = PurchaseInvoices()
        self.journals = Journals()
        self.journal_line_items = JournalLineItem()
        self.purchase_invoice_line_items = PurchaseInvoiceLineItems()
        self.attachments = Attachments()
        self.employees = Employees()
        self.locations = Locations()

        # Get and set the access token
        access_token = self.__refresh_access_token()
        self.set_server_url()
        self.set_batch_url()
        self.update_access_token(access_token)

    def update_access_token(self, access_token: str):
        """
        Update the access token and propagate it to all API objects.
        :param access_token: New access token
        """
        token = 'Bearer {}'.format(access_token)

        api_instances = [
            self.companies,
            self.vendors,
            self.accounts,
            self.purchase_invoices,
            self.journals,
            self.journal_line_items,
            self.purchase_invoice_line_items,
            self.attachments,
            self.employees,
            self.locations
        ]

        # Update access tokens in all API instances
        for api in api_instances:
            api.change_access_token(token)

    def set_batch_url(self):
        """
        Set the Batch URL in all API objects.
        """
        batch_url = self.BASE_URL.format(environment=self.__environment)

        batch_url = '{0}{1}'.format(batch_url, '/$batch')

        api_instances = [
            self.companies,
            self.vendors,
            self.accounts,
            self.purchase_invoices,
            self.journals,
            self.journal_line_items,
            self.purchase_invoice_line_items,
            self.attachments,
            self.employees,
            self.locations
        ]

        # Set batch URL for all API instances
        for api in api_instances:
            api.set_batch_url(batch_url)

    def set_server_url(self):
        """
        Set the Base URL in all API objects.
        """
        base_url = self.BASE_URL.format(environment=self.__environment)

        if self.__company_id:
            base_url = '{0}{1}'.format(base_url, '/companies({0})'.format(self.__company_id))

        api_instances = [
            self.companies,
            self.vendors,
            self.accounts,
            self.purchase_invoices,
            self.journals,
            self.journal_line_items,
            self.purchase_invoice_line_items,
            self.attachments,
            self.employees,
            self.locations
        ]

        # Set base URL for all API instances
        for api in api_instances:
            api.set_server_url(base_url)

    def __refresh_access_token(self):
        """
        Refresh the access token using the refresh token.
        :return: New access token
        """
        token_url = self.TOKEN_URL

        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        data = {
            'grant_type': 'refresh_token',
            'refresh_token': self.__refresh_token,
            'client_id': self.__client_id,
            'client_secret': self.__client_secret
        }

        response = requests.post(token_url, headers=headers, data=data)

        # Handle different response cases
        if response.status_code == 200:
            token = json.loads(response.text)
            self._refresh_token = token['refresh_token']
            return token['access_token']

        elif response.status_code == 400:
            error_msg = json.loads(response.text)['error']

            if error_msg == 'invalid_client':
                raise WrongParamsError('Invalid client ID or client secret or refresh token')

            if error_msg == 'invalid_grant':
                raise InvalidTokenError('Invalid refresh token')

        elif response.status_code == 500:
            raise InternalServerError('Internal server error')

        # Raise a general DynamicsError for other status codes
        raise DynamicsError('Status code {0}'.format(response.status_code), response.text)

    @property
    def refresh_token(self):
        """
        Get the refresh_token property.
        :return: Refresh token
        """
        return self.__refresh_token
