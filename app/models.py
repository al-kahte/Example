class User:
    """
    Represents a user in the system.

    Attributes:
        username (str): The user's username.
        email (str): The user's email address.
        password (str): The user's password.
    """

    def __init__(self,username, email, password):
        """
        Initializes a new instance of the User class.

        Args:
            username (str): The user's username.
            email (str): The user's email address.
            password (str): The user's password.
        """
        self.username = username
        self.email = email
        self.password = password
