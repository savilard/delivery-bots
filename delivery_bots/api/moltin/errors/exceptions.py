class MoltinError(Exception):
    """Exception raised for Moltin errors."""

    def __init__(self, message):
        """Moltin error init."""
        self.message = message

    def __str__(self):
        """Moltin error str."""
        return repr(self.message)
