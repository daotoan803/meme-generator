from abc import ABC, abstractmethod
from typing import List

from quote_engine.quote_model import QuoteModel


class IngestorInterface(ABC):
    """An abstract base class for different file ingestors.

    Provides the interface to check file types and parse them into QuoteModel
    instances.
    """

    allowed_extensions: List[str] = []

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """Check if the file extension is supported for ingestion.

        Args:
            path (str): The file path to check.

        Returns:
            bool: True if the file can be ingested, False otherwise.
        """
        ext = path.split('.')[-1]
        return ext in cls.allowed_extensions

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse a file to extract quotes and return a list of QuoteModel
        instances.

        Args:
            path (str): The file path to parse.

        Returns:
            List[QuoteModel]: A list of extracted QuoteModel instances.
        """
