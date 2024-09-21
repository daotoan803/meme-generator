import subprocess
from typing import List

from quote_engine.quote_model import QuoteModel

from .ingestor_interface import IngestorInterface


class PDFIngestor(IngestorInterface):
    """Ingestor for PDF files using xpdf's pdftotext."""

    allowed_extensions = ['pdf']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """
        Parse PDF file and return a list of QuoteModel objects.

        Args:
            path (str): The file path to the PDF file.

        Returns:
            List[QuoteModel]: A list of QuoteModel objects extracted from the
            PDF file.
        """
        if not cls.can_ingest(path):
            raise ValueError('Cannot ingest exception')

        # Use subprocess to call pdftotext
        temp_txt_path = f"{path}.txt"
        subprocess.call(['pdftotext', path, temp_txt_path])

        quotes = []
        with open(temp_txt_path, 'r', encoding='utf8') as file:
            for line in file.readlines():
                line = line.strip('\n\r').strip()
                if len(line) > 0:
                    parse = line.split(' - ')
                    if len(parse) == 2:
                        new_quote = QuoteModel(parse[0], parse[1])
                        quotes.append(new_quote)

        return quotes
