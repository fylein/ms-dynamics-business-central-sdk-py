from dataclasses import dataclass
from datetime import date

@dataclass
class JournalLineItemsPayload:
    'accountNumber': str
    'postingDate': date
    'documentNumber': str
    'externalDocumentNumber': str
    'amount': float
    'description': str
    'comment': str
    'taxCode': str
    'balancingAccountNumber': str


