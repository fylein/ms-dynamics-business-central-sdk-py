from typing import BinaryIO

from .api_base import ApiBase


class JournalLineItem(ApiBase):
    """Class for PurchaseInvoice APIs."""

    GET_JOURNAL_LINE_ITEMS = '/journals({0})/journalLines'
    POST_JOURNAL_LINE_ITEMS = '/journals({0})/journalLines'

    def get_all(self, jounal_id, **kwargs):
        """
        Get Journal Line Items
        :return: returns all companies
        """
        return self._get_request({
            **kwargs
        }, JournalLineItem.GET_JOURNAL_LINE_ITEMS.format(jounal_id))['value']

    def post(self, journal_id, data):
        """
        Create Journal Line Item
        :param data:
        :return:
        """
        return self._post_request(data, JournalLineItem.POST_JOURNAL_LINE_ITEMS.format(journal_id))
