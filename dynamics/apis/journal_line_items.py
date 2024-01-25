from typing import BinaryIO

from .api_base import ApiBase


class JournalLineItem(ApiBase):
    """Class for Journal LineItem APIs."""

    GET_JOURNAL_LINE_ITEMS = '/journals({0})/journalLines'
    POST_JOURNAL_LINE_ITEMS = '/journals({0})/journalLines'
    BULK_POST_JOURNAL_LINEITEM = 'journals({0})/journalLines'
    DELETE_JOURNAL_LINE_ITEMS = '/journalLines({0})'

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
    
    def delete(self, jounral_lineitem_id: str, **kwargs):
        """
        Delete Journal Line Item
        :param jounral_lineitem_id:
        :param kwargs:
        :return:
        """
        return self._delete_request({**kwargs}, JournalLineItem.DELETE_JOURNAL_LINE_ITEMS.format(jounral_lineitem_id))

    def bulk_post(self, journal_id: str, line_items: list, company_id: str, isolation: str = 'snapshot'):
        """
        Create Journal LineItems in bulk.

        :param journal_id: The ID of the journal.
        :param line_items: A list of line items to be added to the journal line items.
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
                "url": JournalLineItem.BULK_POST_JOURNAL_LINEITEM.format(journal_id),
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
            company_id=company_id
        )
