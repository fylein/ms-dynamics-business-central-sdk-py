from dataclasses import dataclass, asdict
from datetime import date

@dataclass
class PurchaseInvoicePayload:
    invoiceDate: date
    vendorInvoiceNumber: int
    vendorId: str
