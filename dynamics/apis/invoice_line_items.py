from .api_base import ApiBase
from .invoices import PurchaseInvoices


class PurchaseInvoiceLineItems(ApiBase):
    """Class for PurchaseInvoiceLineItmes APIs."""

    GET_PURCHASE_INVOICE_LINEITEMS = '/purchaseInvoices({0})/purchaseInvoiceLines'
    POST_PURCHASE_INVOICE_LINEITEM = '/purchaseInvoices({0})/purchaseInvoiceLines'
    BULK_POST_PURCHASE_INVOICE_LINEITEM = 'purchaseInvoices({0})/purchaseInvoiceLines'
    DELETE_PURCHASE_INVOICE_LINEITEM = '/purchaseInvoiceLines({0})'

    def __init__(self):
        self.__company_id = None

    def set_company_id(self, company_id):
        """Set the company id dynamically upon creating a connection

        Parameters:
            company_id(str): The current company id
        """
        self.__company_id = company_id


    def get_all(self, purchase_invoice_id: str, **kwargs):
        """
        Get all purchase invoice line items
        :return: returns all companies
        """
        return self._get_request({
            **kwargs
        }, PurchaseInvoiceLineItems.GET_PURCHASE_INVOICE_LINEITEMS.format(purchase_invoice_id))['value']

    def post(self, purchase_invoice_id: str, data):
        """
        Create PurchaseInvoice LineItem
        :param purchase_invoice_id:
        :param data:
        :return:
        """
        return self._post_request(
            data, PurchaseInvoiceLineItems.POST_PURCHASE_INVOICE_LINEITEM.format(purchase_invoice_id)
        )

    def delete(self, purchase_invoice_lineitem_id: str, **kwargs):
        """
        Delete PurchaseInvoiceLineItem
        :param purchase_invoice_lineitem_id:
        :param kwargs:
        :return:
        """
        return self._delete_request({**kwargs}, PurchaseInvoiceLineItems.DELETE_PURCHASE_INVOICE_LINEITEM.format(purchase_invoice_lineitem_id))

    def bulk_post(self, purchase_invoice_id: str, line_items: list, isolation: str = 'snapshot'):
        """
        Create PurchaseInvoice LineItems in bulk.

        :param purchase_invoice_id: The ID of the purchase invoice.
        :param line_items: A list of line items to be added to the purchase invoice.
        :return: Bulk response containing the results of the bulk post operation.
        """
        # Prepare payload for bulk post
        bulk_payload = []
        for line_item in line_items:
            # Prepare payload for each line item
            line_item_payload = {
                "method": "POST",
                "url": PurchaseInvoiceLineItems.BULK_POST_PURCHASE_INVOICE_LINEITEM.format(purchase_invoice_id),
                "headers": {
                    "CompanyId": self.__company_id,
                    "Content-Type": "application/json",
                    "If-Match": "*"
                },
                "body": line_item
            }
            bulk_payload.append(line_item_payload)

        # Create a bulk payload containing all line item requests
        bulk_request_payload = {'requests': bulk_payload}

        # Make the bulk post request
        bulk_payload_response = self._bulk_post_request(bulk_request_payload, isolation)

        # Return the bulk response if all line items were created successfully
        return bulk_payload_response
