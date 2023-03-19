class UserRepository:
    """
    UserRepository is an in-memory repository that stores user data in a Python dictionary.

    Attributes:
        users (dict): A dictionary that maps usernames to User objects.
    """

    def __init__(self):
        """
        Constructs a new UserRepository instance with an empty users dictionary.
        """
        self.users = {}

    def add_user(self, user):
        """
        Adds a new user to the repository.

        Args:
            user (User): The User object to add.

        Raises:
            ValueError: If a user with the same username already exists in the repository.
        """
        if user.username in self.users:
            raise ValueError('User already exists')
        self.users[user.username] = user

    def get_user(self, username):
        """
        Returns a User object with the specified username.

        Args:
            username (str): The username to look up.

        Returns:
            User: The User object with the specified username, or None if no such user exists.
        """
        return self.users.get(username)
