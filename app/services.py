from .exceptions import UserAlreadyExistsError
from .models import User
from .repositories import UserRepository

class UserService:
    """A service class for user-related functionality.

    Attributes:
        user_repository (UserRepository): The repository used to manage user data.
    """

    def __init__(self, user_repository: UserRepository) -> None:
        """Initializes a new instance of the UserService class.

        Args:
            user_repository (UserRepository): The repository used to manage user data.
        """
        self.user_repository = user_repository

    def register_user(self, username: str, email: str, password: str) -> User:
        """Registers a new user with the specified username, email, and password.

        Args:
            username (str): The username for the new user.
            email (str): The email address for the new user.
            password (str): The password for the new user.

        Returns:
            User: The newly registered user.

        Raises:
            UserAlreadyExistsError: If a user with the specified username already exists.
        """
        if self.user_repository.get_user(username):
            raise UserAlreadyExistsError('Username already exists')
        user = User(username, email, password)
        self.user_repository.add_user(user)
        return user

    def authenticate_user(self, username: str, password: str) -> User:
        """Authenticates a user with the specified username and password.

        Args:
            username (str): The username of the user to authenticate.
            password (str): The password of the user to authenticate.

        Returns:
            User: The authenticated user if the username and password are correct, otherwise None.
        """
        user = self.user_repository.get_user(username)
        if not user or user.password != password:
            return None
        return user
