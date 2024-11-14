from .api_base import ApiBase


class DimensionSetLines(ApiBase):
    """Class for Dimension Set Lines APIs."""

    JOUNRAL_ENTRY = '/journalLines({0})/dimensionSetLines'
    PURCHASE_INVOICE = '/purchaseInvoiceLines({0})/dimensionSetLines'

    def post_journal_entry(self, journal_line_item_id: str, data: dict):
        """
        Create dimension set line for a journal line item
        Parameters:
            journal_line_item_id: Id of the Journal Line Item (str)
            data: Payload to be posted (dict)
        """
        
        return self._post_request(
            data, DimensionSetLines.JOUNRAL_ENTRY.format(journal_line_item_id)
        )

    def post_purchase_invoice(self, purchase_invoice_item_id: str, data: dict):
        """
        Create dimension set line for a purchase invoice item
        Parameters:
            purchase_invoice_item_id: Id of the Purchase Invoice Item (str)
            data: Payload to be posted (dict)
        :return:
        """
        
        return self._post_request(
            data, DimensionSetLines.PURCHASE_INVOICE.format(purchase_invoice_item_id)
        )
