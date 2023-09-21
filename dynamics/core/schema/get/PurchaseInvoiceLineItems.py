from dataclasses import dataclass 
from datetime import date

@dataclass
class PuchaseInvoiceLineItemResponse:
    'id': str
    'documentId': str
    'sequence': int
    'itemId': str
    'accountId': str
    'lineType': str
    'lineObjectNumber': str
    'description': str
    'description2': str
    'unitOfMeasureId': str
    'unitOfMeasureCode': str
    'unitCost': float
    'quantity': int
    'discountAmount': float
    'discountPercent': float
    'discountAppliedBeforeTax': bool
    'amountExcludingTax': float
    'taxCode': str
    'taxPercent': float
    'totalTaxAmount': float
    'amountIncludingTax': float
    'invoiceDiscountAllocation': float
    'netAmount': float
    'netTaxAmount': float
    'netAmountIncludingTax': float
    'expectedReceiptDate': date
    'itemVariantId': str
    'locationId': str
