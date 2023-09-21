from dataclasses import dataclass 
from datetime import date

@dataclass
class PurchaseInvoiceResponse:
    'id': str
    'number': str
    'invoiceDate': date
    'postingDate': date
    'dueDate': date
    'vendorInvoiceNumber': str
    'vendorId': str
    'vendorNumber': str
    'vendorName': str
    'payToName': str
    'payToContact': str
    'payToVendorId': str
    'payToVendorNumber': str
    'shipToName': str
    'shipToContact': str
    'buyFromAddressLine1': str
    'buyFromAddressLine2': str
    'buyFromCity': str
    'buyFromCountry': str
    'buyFromState': str
    'buyFromPostCode': str
    'shipToAddressLine1': str
    'shipToAddressLine2': str
    'shipToCity': str
    'shipToCountry': str
    'shipToState': str
    'shipToPostCode': str
    'payToAddressLine1': str
    'payToAddressLine2': str
    'payToCity': str
    'payToCountry': str
    'payToState': str
    'payToPostCode': str
    'shortcutDimension1Code': str
    'shortcutDimension2Code': str
    'currencyId': str
    'currencyCode': str
    'orderId': str
    'orderNumber': str
    'pricesIncludeTax': bool
    'discountAmount': float
    'discountAppliedBeforeTax': bool
    'totalAmountExcludingTax': float
    'totalTaxAmount': float
    'totalAmountIncludingTax': float
    'status': str
    'lastModifiedDateTime': date
