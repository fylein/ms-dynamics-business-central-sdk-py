from typing import BinaryIO

from .api_base import ApiBase


class PurchaseInvoices(ApiBase):
    """Class for PurchaseInvoice APIs."""

    GET_PURCHASE_INVOICES = '/purchaseInvoices'
    POST_PURCHASE_INVOICE = '/purchaseInvoices'
    DELETE_PURCHASE_INVOICE = '/purchaseInvoices({0})'

    def get_all(self, **kwargs):
        """
        Get all purchase invoices
        :return: returns all companies
        """
        return self._get_request({
            **kwargs
        }, PurchaseInvoices.GET_PURCHASE_INVOICES)['value']

    def post(self, data):
        """
        Create PurchaseInvoice
        :param data:
        :return:
        """
        return self._post_request(data, PurchaseInvoices.POST_PURCHASE_INVOICE)

    def delete(self, purchase_invoice_id: str, **kwargs):
        """
        Delete PurchaseInvoice
        :param purchase_invoice_id:
        :param kwargs:
        :return:
        """
        return self._delete_request({**kwargs}, PurchaseInvoices.DELETE_PURCHASE_INVOICE.format(purchase_invoice_id))
