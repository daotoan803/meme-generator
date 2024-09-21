from typing import List

import docx

from quote_engine.quote_model import QuoteModel

from .ingestor_interface import IngestorInterface


class DocxIngestor(IngestorInterface):
    """Ingest quotes from a DOCX file.

    Methods:
        can_ingest: Check if the file can be ingested based on its extension.
        parse: Parse the DOCX file and return a list of QuoteModel instances.
    """

    allowed_extensions = ['docx']

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """Check if the file extension is DOCX.

        Args:
            path (str): The file path to check.

        Returns:
            bool: True if the file is a DOCX, otherwise False.
        """
        ext = path.split('.')[-1]
        return ext in cls.allowed_extensions
    
    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse a docx file to extract quotes.

        Args:
            path (str): The path to the docx file.

        Returns:
            List[QuoteModel]: A list of QuoteModel instances extracted from
            the docx file.
        """
        if not cls.can_ingest(path):
            raise Exception('Cannot ingest exception')

        quotes = []
        doc = docx.Document(path)

        for para in doc.paragraphs:
            if para.text != "":
                parse = para.text.split(' - ')
                if len(parse) == 2:
                    new_quote = QuoteModel(parse[0], parse[1])
                    quotes.append(new_quote)

        return quotes
