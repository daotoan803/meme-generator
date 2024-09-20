class QuoteModel:
    """A class to represent a quote.

    Attributes:
        body (str): The text of the quote.
        author (str): The author of the quote.
    """

    def __init__(self, body: str, author: str):
        """Initialize a QuoteModel object with a quote body and its author.

        Args:
            body (str): The text of the quote.
            author (str): The author of the quote.
        """
        self.body = body
        self.author = author

    def __str__(self):
        """Return a string representation of the quote."""
        return f'"{self.body}" - {self.author}'
    
    def __repr__(self):
        """Return a technical string representation of the QuoteModel."""
        return f'QuoteModel(body={self.body}, author={self.author})'
