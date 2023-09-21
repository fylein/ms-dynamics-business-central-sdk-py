from dataclasses import dataclass
from datetime import date

@dataclass
class JournalResponse:
    'id': str
    'code': str
    'displayName': str
    'templateDisplayName': str
    'lastModifiedDateTime': date
    'balancingAccountId': str
    'balancingAccountNumber': str
