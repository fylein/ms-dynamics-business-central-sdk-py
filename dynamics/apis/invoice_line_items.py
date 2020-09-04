from .api_base import ApiBase


class PurchaseInvoiceLineItems(ApiBase):
    """Class for PurchaseInvoiceLineItmes APIs."""

    GET_PURCHASE_INVOICE_LINEITEMS = '/purchaseInvoices({0})/purchaseInvoiceLines'
    POST_PURCHASE_INVOICE_LINEITEM = '/purchaseInvoices({0})/purchaseInvoiceLines'

    def get(self, purchase_invoice_id: str, **kwargs):
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
