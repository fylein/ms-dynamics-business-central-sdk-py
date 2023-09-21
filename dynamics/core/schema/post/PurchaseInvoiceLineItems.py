from dataclasses import dataclass, asdict
from datetime import date

@dataclass
class PurchaseInvoiceLineItemPayload:
    sequence: int
    lineType: str
    lineObjectNumber: str
    unitCost: float
    quantity: int
    locationId: str
