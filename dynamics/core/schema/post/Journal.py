from dataclasses import dataclass, asdict
from datetime import date

@dataclass
class JounalPayload:
  'code': str
  'displayName': str
  'templateDisplayName': str