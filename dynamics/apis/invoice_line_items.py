from .api_base import ApiBase
from .invoices import PurchaseInvoices


class PurchaseInvoiceLineItems(ApiBase):
    """Class for PurchaseInvoiceLineItmes APIs."""

    GET_PURCHASE_INVOICE_LINEITEMS = '/purchaseInvoices({0})/purchaseInvoiceLines'
    POST_PURCHASE_INVOICE_LINEITEM = '/purchaseInvoices({0})/purchaseInvoiceLines'
    BULK_POST_PURCHASE_INVOICE_LINEITEM = 'purchaseInvoices({0})/purchaseInvoiceLines'
    DELETE_PURCHASE_INVOICE_LINEITEM = '/purchaseInvoiceLines({0})'


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

    def bulk_post(self, purchase_invoice_id: str, line_items: list, company_id: str, isolation: str = 'snapshot'):
        """
        Create PurchaseInvoice LineItems in bulk.

        :param purchase_invoice_id: The ID of the purchase invoice.
        :param line_items: A list of line items to be added to the purchase invoice.
        :param company_id: The ID of the company. (batch requests mandatorily need this)
        :param isolation: The isolation level of the bulk post request.
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
                    "CompanyId": company_id,
                    "Content-Type": "application/json",
                    "If-Match": "*"
                },
                "body": line_item
            }
            bulk_payload.append(line_item_payload)

        # Create a bulk payload containing all line item requests
        bulk_request_payload = {'requests': bulk_payload}

        # Make the bulk post request
        return self._bulk_post_request(
            data=bulk_request_payload,
            isolation=isolation,
            purchase_invoice_id=purchase_invoice_id,
            company_id=company_id
        )
