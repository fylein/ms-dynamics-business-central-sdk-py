from dataclasses import dataclass, asdict
from datetime import date

@dataclass
class PurchaseInvoicePayload:
    invoiceDate: date
    vendorInvoiceNumber: int
    vendorId: str

@dataclass
class PurchaseInvoiceLineItemPayload:
    sequence: int
    lineType: str
    lineObjectNumber: str
    unitCost: float
    quantity: int
    locationId: str