"""Customer records, as the accounts service sends them."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Customer:
    id: int
    name: str
    email: str
    locale: str = "en"
