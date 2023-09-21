from dataclasses import dataclass
from datetime import date

@dataclass
class JournalLineItemResponse:
    'id': str
    'journalId': str
    'journalDisplayName': str
    'lineNumber': int
    'accountType': str
    'accountId': str
    'accountNumber': str
    'postingDate': date
    'documentNumber': str
    'externalDocumentNumber': str
    'amount': float
    'description': str
    'comment': str
    'taxCode': str
    'balanceAccountType': str
    'balancingAccountId': str
    'balancingAccountNumber': str
    'lastModifiedDateTime': date