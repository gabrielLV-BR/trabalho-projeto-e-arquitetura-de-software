
from dataclasses import dataclass

@dataclass
class PaginationArgs():
    page: int
    page_size: int