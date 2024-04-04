"""
A module providing a simple console utility for printing messages with color using colorama.
"""

from colorama import init, Fore


class Console:
    """
    A simple console utility for printing messages with color using colorama.
    """

    def __init__(self):
        """Initialize the Console class."""
        # Initialize colorama
        init(autoreset=True)


    def log(self, message: str, end: str = None) -> None:
        """Prints a normal message in white color.

        Args:
            message (str): The message to be printed.
            end (str, optional): The string to append after the message. Defaults to None.
        """
        print(message, end=end)


    def info(self, message: str, end: str = None) -> None:
        """Prints an informational message in blue color.

        Args:
            message (str): The message to be printed.
            end (str, optional): The string to append after the message. Defaults to None.
        """
        print(f"{Fore.BLUE}{message}", end=end)


    def warn(self, message: str, end: str = None) -> None:
        """Prints a warning message in yellow color.

        Args:
            message (str): The message to be printed.
            end (str, optional): The string to append after the message. Defaults to None.
        """
        print(f"{Fore.YELLOW}{message}", end=end)


    def error(self, message: str, end: str = None) -> None:
        """Prints an error message in red color.

        Args:
            message (str): The message to be printed.
            end (str, optional): The string to append after the message. Defaults to None.
        """
        print(f"{Fore.RED}{message}", end=end)

  
    def success(self, message: str, end: str = None) -> None:
        """Prints a success message in green color.

        Args:
            message (str): The message to be printed.
            end (str, optional): The string to append after the message. Defaults to None.
        """
        print(f"{Fore.GREEN}{message}", end=end)


    def secondary(self, message: str, end: str = None) -> None:
        """Prints a secondary message in gray color.

        Args:
            message (str): The message to be printed.
            end (str, optional): The string to append after the message. Defaults to None.
        """
        print(f"{Fore.LIGHTBLACK_EX}{message}", end=end)
