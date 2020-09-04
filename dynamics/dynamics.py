from base64 import b64encode

from .apis import *


class Dynamics:
    """The main class which creates a connection with Dynamics APIs.
    """

    TOKEN_URL = '{}/oauth/token'
    BASE_URL = 'https://api.businesscentral.dynamics.com/v2.0/{0}/{1}/api/v1.0/companies({2})'

    def __init__(self, user_name: str, web_api_key: str, tenant_domain: str, environment: str, company_id: str):
        """
        Constructor to initialize the SDK
        :param user_name: Dynamics Username
        :param web_api_key: Dynamics Web API key
        :param tenant_domain: Dynamics Tenant Domain
        :param: environment: sandbox / production
        :param company_id: Dynamics Company Id
        """
        self.__base_url = self.BASE_URL.format(tenant_domain, environment, company_id)
        self.__user_name = user_name
        self.__web_api_key = web_api_key

        # create an object for each api
        self.vendors = Vendors()
        self.accounts = Accounts()
        self.purchase_invoices = PurchaseInvoices()
        self.purchase_invoice_line_items = PurchaseInvoiceLineItems()
        self.attachments = Attachments()

        # get the access token
        self.update_access_token()
        self.set_server_url()

    def update_access_token(self):
        """Update the access token and change it in all API objects."""

        token = self.__get_token()

        self.vendors.change_access_token(token)
        self.accounts.change_access_token(token)
        self.purchase_invoices.change_access_token(token)
        self.purchase_invoice_line_items.change_access_token(token)
        self.attachments.change_access_token(token)

    def set_server_url(self):
        """Set the Base URL in all API objects."""

        base_url = self.__base_url

        self.vendors.set_server_url(base_url)
        self.accounts.set_server_url(base_url)
        self.purchase_invoices.set_server_url(base_url)
        self.purchase_invoice_line_items.set_server_url(base_url)
        self.attachments.set_server_url(base_url)

    def __get_token(self):
        """Get the access token using a HTTP post.

        Returns:
            A new access token.
        """
        token_string = '{0}:{1}'.format(self.__user_name, self.__web_api_key)

        basic_token = b64encode(token_string.encode()).decode("ascii")

        basic_token = 'Basic {}'.format(basic_token)

        return basic_token
