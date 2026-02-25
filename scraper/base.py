import dataclasses
import datetime

import requests
from requests.adapters import HTTPAdapter, Retry

UNKNOWN_DATE = datetime.date.min


@dataclasses.dataclass
class DeprecationEntry:
    provider: str
    model_name: str
    model_id: str = ""
    deprecated_date: datetime.date = UNKNOWN_DATE
    shutdown_date: datetime.date = UNKNOWN_DATE
    replacement: str = ""
    status: str = "active"

    def has_deprecated_date(self) -> bool:
        return self.deprecated_date != UNKNOWN_DATE

    def has_shutdown_date(self) -> bool:
        return self.shutdown_date != UNKNOWN_DATE

    def to_dict(self) -> dict:
        d = dataclasses.asdict(self)
        for key in ("deprecated_date", "shutdown_date"):
            val = d[key]
            if val == UNKNOWN_DATE:
                d[key] = ""
            elif isinstance(val, datetime.date):
                d[key] = val.isoformat()
        return d

    @classmethod
    def from_dict(cls, d: dict) -> "DeprecationEntry":
        d = dict(d)
        for key in ("deprecated_date", "shutdown_date"):
            val = d.get(key, "")
            if isinstance(val, str) and val:
                d[key] = datetime.date.fromisoformat(val)
            else:
                d[key] = UNKNOWN_DATE
        return cls(**d)


def create_session() -> requests.Session:
    session = requests.Session()
    retries = Retry(total=3, backoff_factor=1, status_forcelist=[429, 500, 502, 503, 504])
    adapter = HTTPAdapter(max_retries=retries)
    session.mount("https://", adapter)
    session.mount("http://", adapter)
    session.headers.update(
        {
            "User-Agent": "ModelDeprecationTracker/1.0 (+https://github.com/model-deprecation-tracker)"
        }
    )
    return session


def fetch_page(url: str, session: requests.Session = None) -> str:
    if session is None:
        session = create_session()
    response = session.get(url, timeout=30)
    response.raise_for_status()
    return response.text
