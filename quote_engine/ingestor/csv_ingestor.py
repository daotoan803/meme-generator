from typing import List

import pandas as pd

from quote_engine.ingestor.ingestor_interface import IngestorInterface
from quote_engine.quote_model import QuoteModel


class CSVIngestor(IngestorInterface):
    """Ingest quotes from a CSV file.

    Methods:
        can_ingest: Check if the file can be ingested based on its extension.
        parse: Parse the CSV file and return a list of QuoteModel instances.
    """

    allowed_extensions = ['csv']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse a CSV file to extract quotes.

        Args:
            path (str): The path to the CSV file.

        Returns:
            List[QuoteModel]: A list of QuoteModel instances extracted from
            the CSV file.
        """
        if not cls.can_ingest(path):
            raise ValueError(
                f"Cannot ingest file with extension {path.split('.')[-1]}")

        quotes = []
        df = pd.read_csv(path)
        for index, row in df.iterrows():
            new_quote = QuoteModel(row['body'], row['author'])
            quotes.append(new_quote)
        return quotes
