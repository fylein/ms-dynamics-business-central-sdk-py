from typing import BinaryIO

from .api_base import ApiBase


class Journals(ApiBase):
    """Class for PurchaseInvoice APIs."""

    GET_JOURNALS = '/journals'
    POST_JOURNALS = '/journals'
    DELETE_JOURNALS = '/journals({0})'

    def get_all(self, **kwargs):
        """
        Get all purchase invoices
        :return: returns all companies
        """
        return self._get_request({
            **kwargs
        }, Journals.GET_JOURNALS)['value']

    def post(self, data):
        """
        Create PurchaseInvoice
        :param data:
        :return:
        """
        return self._post_request(data, Journals.POST_JOURNALS)
    
    def delete(self, journal_id: str, **kwargs):
        """
        Delete Journals
        :param journal_id:
        :param kwargs:
        :return:
        """
        return self._delete_request({**kwargs}, Journals.DELETE_JOURNALS.format(journal_id))
