
from typing import List

from quote_engine.ingestor.docx_ingestor import DocxIngestor
from quote_engine.ingestor.pdf_ingestor import PDFIngestor

from .ingestor.csv_ingestor import CSVIngestor
from .ingestor.text_ingestor import TextIngestor
from .quote_model import QuoteModel


class Ingestor:
    """Main class to ingest quotes from different file formats.

    It checks the file type and delegates parsing to the appropriate ingestor.

    Attributes:
        ingestors (List): A list of available ingestor classes.

    Methods:
        parse: Parse a file based on its type using the appropriate ingestor.
    """

    ingestors = [CSVIngestor, TextIngestor, PDFIngestor, DocxIngestor]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse the file using the appropriate ingestor.

        Args:
            path (str): The path to the file to be ingested.

        Returns:
            List[QuoteModel]: A list of QuoteModel instances extracted from
            the file.
        """
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)
        raise ValueError(f"No valid ingestor found for file: {path}")
