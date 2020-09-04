from typing import BinaryIO

from .api_base import ApiBase


class PurchaseInvoices(ApiBase):
    """Class for PurchaseInvoice APIs."""

    GET_PURCHASE_INVOICES = '/purchaseInvoices'
    POST_PURCHASE_INVOICE = '/purchaseInvoices'

    def get(self, **kwargs):
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
