from typing import List

from quote_engine.ingestor.ingestor_interface import IngestorInterface
from quote_engine.quote_model import QuoteModel


class TextIngestor(IngestorInterface):
    """Ingest quotes from a text file.

    Methods:
        can_ingest: Check if the file can be ingested based on its extension.
        parse: Parse the text file and return a list of QuoteModel instances.
    """
    allowed_extensions = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse a text file to extract quotes.

        Args:
            path (str): The path to the text file.

        Returns:
            List[QuoteModel]: A list of QuoteModel instances extracted from
            the text file.
        """
        if not cls.can_ingest(path):
            raise ValueError(
                f"Cannot ingest file with extension {path.split('.')[-1]}")

        quotes = []
        with open(path, 'r', encoding='utf8') as file:
            for line in file.readlines():
                if line.strip():  # Ignore empty lines
                    body, author = line.strip().split(' - ')
                    quotes.append(QuoteModel(body, author))
        return quotes
